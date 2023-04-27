"""Watch for iss - satellit on the Earth orbit.
Uses requests: 'http://api.open-notify.org/iss-now.json' for geting iss actual cootdinates.
Uses turtele module for show moving of the iss."""

import requests, json, turtle, time


num_of_start = 0


def move_iss(lat, long):
    global iss

    iss.goto(long, lat)
    iss.pendown()


def setup(window):
    global iss

    window.setup(1024, 768)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)

    iss = turtle.Turtle()
    iss.shape('turtle')
    iss.color('red')


def track_iss():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    if (response.status_code == 200):
        response_dictonary = json.loads(response.text)
        position = response_dictonary['iss_position']
        lat = float(position['latitude'])
        long = float(position['longitude'])
        move_iss(lat, long)
    else:
        print('We have some problem', response.status_code)
    widget = turtle.getcanvas()
    widget.after(5000, track_iss())


def main():

    try:
        global iss
        global num_of_start

        screen = turtle.Screen()
        setup(screen)
        iss.penup()
        track_iss()

    except:

        if num_of_start < 2:
            time.sleep(10)
            num_of_start += 1
            main()
        else:
            print('Error hepend!!!')
            exit()


if __name__ == '__main__':
    main()
    turtle.mainloop()
