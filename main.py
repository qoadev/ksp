import time
import krpc
import matplotlib.pyplot as plt

conn = krpc.connect(name='Vessel speed')
vessel = conn.space_center.active_vessel
obt_frame = vessel.orbit.body.non_rotating_reference_frame
srf_frame = vessel.orbit.body.reference_frame
sec = 0

speede_to_time = {}
speed1 = []



conn = krpc.connect(name='User Interface Example')
canvas = conn.ui.stock_canvas

# Get the size of the game window in pixels
screen_size = canvas.rect_transform.size

# Add a panel to contain the UI elements
panel = canvas.add_panel()

# Position the panel on the left of the screen
rect = panel.rect_transform
rect.size = (200, 100)
rect.position = (110-(screen_size[0]/2), 0)

# Add a button to set the throttle to maximum
button = panel.add_button("build a graph")
button.rect_transform.position = (0, 20)

button_clicked = conn.add_stream(getattr, button, 'clicked')

time.sleep(5)
while True:
    obt_speed = vessel.flight(obt_frame).speed
    srf_speed = vessel.flight(srf_frame).speed

    sec += 1
    print('Orbital speed = %.1f m/s, Surface speed = %.1f m/s' % (obt_speed, srf_speed), sec)
    #  speede_to_time[sec] = srf_speed
    speed1.append(srf_speed)
    time.sleep(1)

    if button_clicked():
        vessel.control.throttle = 1
        button.clicked = False
        fig, ax = plt.subplots()
        ax.set_title("График")
        ax.set_xlabel("t, s")
        ax.set_ylabel("v, m/s")
        ax.grid()
        plt.plot(list(range(0, sec)), speed1)
        plt.show()
        if sec == 800:
            fig, ax = plt.subplots()
            ax.set_title("График")
            ax.set_xlabel("t, s")
            ax.set_ylabel("v, m/s")
            ax.grid()
            plt.plot(list(range(0, sec)), speed1)
            plt.show()
