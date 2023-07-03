# this line imports functionality into our project, so we don't have to write it ourselves!
from flask import Flask, render_template, request, redirect

app = Flask(__name__) # create flask instance

items = []

@app.route('/')     # python decorator, use Flask, when open the home page
def index():        # when open the homepage, Flask will use index function to return helloworld. 
    return 'Hello, world!'

@app.route('/tasks')
def tasks(): 
    tasks = fetch_tasks_from_database()               # Retrieve tasks from the database
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['POST'])    # ‘/add’ is the path used for this route
def add_item():
    item = request.form['item']
    items.append(item)  # append the new item to the list, not stored in the database
    return redirect('/')

@app.route('/')     # By default, route uses the GET method. That only lets the user receive, not send, data.
def checklist():
    return render_template('checklist.html', items=items)

# now, we're creating the update functionality/endpoint
@app.route('/edit/<int:item_id>', methods=['GET','POST'])
def edit_item(item_id):
    item = items[item_id -1] # retrieve the item based on its index

    if request.method == 'POST':
        new_item = request.form['item']
        items[item_id -1] = new_item
        return redirect('/')

    return render_template('edit.html', item=item, item_id=item_id)

# delete
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    del items[item_id - 1]
    return redirect('/')