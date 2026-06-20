from django.shortcuts import render

# Create your views here.

def contact_us(request):
    
    
    return render(request, 'contact/contact_us.html')








# # contact views
# def contact(request):
#     # contact = Contact.objects.all()
    
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the data to the database
#             messages.success(request, 'Your message has been sent successfully!')
#             return redirect('contact')  # Redirect to avoid resubmission on refresh
#     else:
#         form = ContactForm()
        
#     # Pass form fields individually
#     context = {
#         'user_name': form['user_name'],
#         'user_mobile': form['user_mobile'],
#         'user_email': form['user_email'],
#         'user_message': form['user_message']
#     }
    
#     return render(request, 'core/contact.html', context)









# # admin view start here 
# # contact list view 
# @login_required
# @user_passes_test(is_superuser)
# def contact_list(request):
#     messages = Contact.objects.order_by('created_at').all()
    
#     return render(request, 'admin_panel/core/messages.html', {'messages': messages})



# @login_required
# @user_passes_test(is_superuser)
# def message_status_update(request, contact_id):
    
#     messages = Contact.objects.all()
#     message = get_object_or_404(Contact, id=contact_id)
    
#     if request.method == 'POST':
#         form = ContactStatusForm(request.POST, instance=message)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Message status updated successfully.')
#             return redirect('messages')
        
#     else:
#         form = ContactStatusForm(instance=message)
    
#     return render(request, 'admin_panel/core/messages.html', {'form': form, 'messages': messages})










