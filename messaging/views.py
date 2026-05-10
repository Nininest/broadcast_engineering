from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages as django_messages
from core.models import AuditLog
from .models import Message

# Create your views here.

@login_required
def inbox(request):
    msgs = Message.objects.filter(
        recipient=request.user, status='sent', deleted_by_recipient=False
    ).select_related('sender')
    unread = msgs.filter(read=False).count()
    return render(request, 'messaging/inbox.html', {
        'msgs':msgs, 
        'unread':unread,
        'section': 'inbox'
    })

@login_required
def sent_messages(request):
    msgs = Message.objects.filter(
        sender=request.user, status='sent', deleted_by_sender=False
    ).select_related('recipient')
    return render(request, 'messaging/sent.html', {
        'msgs':msgs,
        'section':'sent'
    })

@login_required
def drafts(request):
    msgs = Message.objects.filter(sender=request.user, status='draft').select_related('recipient')
    return render(request, 'messaging/drafts.html', {
        'msgs':msgs,
        'section':'draft'
    })

@login_required
def compose(request, reply_to=None):
    users = User.objects.exclude(pk=request.user.pk)
    initial_recipient=None
    initial_subject = ''
    if reply_to:
        original = get_object_or_404(Message, pk=reply_to, recipient=request.user)
        initial_recipient = original.sender
        initial_subject = f"Re: {original.subject}"
    if request.method == 'POST': 
        recipient_id = request.POST.get('recipient')
        subject = request.POST.get('subject', '').strip()
        body = request.POST.get('body', '').strip()
        action = request.POST.get('action', 'send')
        if not subject or not body or not recipient_id:
            django_messages.error(request, 'Please fill all fields')
        else: 
            try:
                recipient = User.objects.get(pk=recipient_id)
                status = 'draft' if action == 'draft' else 'sent'
                msg = Message.objects.create(
                    sender = request.user, recipient = recipient, 
                    subject = subject, body = body, status = stauts, 
                )
                AuditLog.objects.create(
                    user=request.user, action_type = 'insert', 
                    table_name = 'Message', record_id = msg.id,
                    description = f"Message {'drafted' if status == 'draft' else 'sent'} to {recipient.username}"
                )
                if status == 'sent':
                    django_messages.success(request, f'Message sent to {recipient.get_full_name()}.')
                    return redirect('inbox')
                else:
                    django_messages.success(request, 'Draft saved.')
                    return redirect('drafts')
            except User.DoesNotExist:
                django_messages.error(request, 'Invalid recipient.')
    return render(request, 'messaging/compose.html', {
        'users':users, 
        'initial_recipient':initial_recipient, 
        'initial_subject':initial_subject
    })

@login_required
def view_message(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if msg.recipient == request.user and not msg.read:
        msg.read = True
        msg.save()
    return render(request, 'messaging/view_message.html', {
        'msg':msg
    })

@login_required
def delete_message(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if msg.sender == request.user:
        msg.deleted_by_sender = True
        msg.save()
    elif msg.recipient == request.user:
        msg.deleted_by_recipient = True
        msg.save()
    AuditLog.objects.create(user=request.user, action_type='delete', table_name='Message', record_id=msg.id, description='Message Deleted')
    return redirect('inbox')