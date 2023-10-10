from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'Suman2003@'

# In a real project, you should use a database for storage.
events = []
participants = []
participant_data = []

@app.route('/')
def index():
    return "Welcome to the Event Registration App"

@app.route('/submit_event', methods=['GET', 'POST'])
def submit_event():
    if request.method == 'POST':
        event_name = request.form.get('event_name')
        event_date = request.form.get('event_date')
        event_description = request.form.get('event_description')

        event = {
            'name': event_name,
            'date': event_date,
            'description': event_description,
        }
        events.append(event)
        return redirect('/event_list')
    return render_template('submit_event.html')

@app.route('/event_list')
def event_list():
    return render_template('event_list.html', events=events)

@app.route('/register_participant', methods=['GET', 'POST'])
def register_participant():
    if request.method == 'POST':
        participant_name = request.form.get('participant_name')
        phone_number = request.form.get('phone_number')
        selected_event = request.form.get('event')

        if participant_name and phone_number and selected_event:
            participant = {
                'name': participant_name,
                'phone_number': phone_number,
                'event': selected_event,
            }
            participant_data.append(participant)
            return redirect('/registration_confirmation')

    return render_template('register_participant.html', events=events)

@app.route('/participant_list')
def participant_list():
    return render_template('participant_list.html', participant_data=participant_data)


@app.route('/registration_confirmation')
def registration_confirmation():
    participant_name = session.get('participant_name')
    phone_number = session.get('phone_number')
    selected_event = session.get('selected_event')

    if not (participant_name and phone_number and selected_event):
        return redirect('/register_participant')

    return render_template('registration_confirmation.html', participant_name=participant_name, phone_number=phone_number, selected_event=selected_event)

if __name__ == '__main__':
    app.run(debug=True)

