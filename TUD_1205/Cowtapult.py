# Assignment Four. A simulation of a cow being thrown by a catapult
# Author: Nikolaus Ricker
import math
import pygame as pg
import pygame.time


def catapult(R=10.0, l_0=0.5, theta_stop=math.pi / 3, theta_start=0.0, k_elastic=9000, m_cow=550):
    # ------------------------------------------------------
    # Library
    import matplotlib.pyplot as plt

    # ------------------------------------------------------
    # Constants
    g = 9.81
    t = 0
    dt = 0.0001

    # For first part
    # R = 10
    # theta_stop = math.pi / 3
    # theta_start = 0
    # l_0 = 0.5
    # k_elastic = 9000
    # m_cow = 550

    # For second part
    h0 = 60
    cd = 0.7
    rho_air = 1.225
    rho_cow = 1000

    # ------------------------------------------------------
    # First calculations
    V_cow = m_cow / rho_cow
    r_cow = math.pow(V_cow * 3 / (4 * math.pi), 1 / 3)
    S_cow = math.pi * math.pow(r_cow, 2)
    # ------------------------------------------------------
    # Catapult
    # Initial conditions
    theta = theta_start
    omega = 0
    alpha = 0
    theta_list = []
    omega_list = []
    alpha_list = []
    t_list = []
    Fg = m_cow * g

    while theta <= theta_stop:

        # Components of length elastic
        lx = R * math.cos(theta)
        ly = R * (1 - math.sin(theta))
        l_elastic = math.sqrt(math.pow(lx, 2) + math.pow(ly, 2))

        # Angles
        beta = math.pi/2 - theta
        phi = math.atan(ly / lx)

        # Forces
        if math.fabs(l_elastic) < l_0:
            Fe = 0
        else:
            Fe = k_elastic * (l_elastic - l_0)

        Ft = Fe * math.sin(phi + theta) - Fg * math.sin(beta)

        # Acceleration
        at = Ft / m_cow

        # List
        theta_list.append(theta)
        alpha_list.append(alpha)
        omega_list.append(omega)
        t_list.append(t)

        # New values
        alpha = at / R
        omega += alpha * dt
        theta += omega * dt
        t += dt

    v0 = omega_list[-1] * R
    print(v0)

    # ------------------------------------------------------
    # Trajectory
    vx = v0 * math.sin(theta_list[-1])
    vy = v0 * math.cos(theta_list[-1])

    d1 = rho_air * cd * S_cow / 2
    x = 0
    y = h0
    t = 0
    dt = 0.01
    x_list = []
    y_list = []
    t2_list = []
    vx_list = []
    vy_list = []

    while y > 0:

        ax = -d1 * (vx ** 2) / m_cow

        if vy > 0:
            ay = -g - (d1 * (vy ** 2)) / m_cow
        else:
            ay = -g + (d1 * (vy ** 2)) / m_cow

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

        t += dt

        x_list.append(x)
        y_list.append(y)
        t2_list.append(t)
        vx_list.append(vx)
        vy_list.append(vy)
    # ------------------------------------------------------
    # Plots

    # plt.subplot(311)
    # plt.plot(t_list, theta_list)
    # plt.title("Theta")
    # plt.subplot(312)
    # plt.plot(t_list, omega_list)
    # plt.title("Omega")
    # plt.subplot(313)
    # plt.plot(t_list[1:], alpha_list[1:])
    # plt.title("Alpha")
    # plt.show()

    # plt.subplot(421)
    # plt.plot(t2_list, x_list)
    # plt.title("x Displacement")
    # plt.subplot(422)
    # plt.plot(t2_list, y_list)
    # plt.title("y Displacement")
    # plt.subplot(423)
    # plt.plot(t2_list, vx_list)
    # plt.title("x Velocity")
    # plt.subplot(424)
    # plt.plot(t2_list, vy_list)
    # plt.title("y Velocity")
    # plt.show()

    plt.subplot(321)
    plt.plot(t2_list, vx_list)
    plt.title("x Velocity")
    plt.subplot(322)
    plt.plot(t2_list, vy_list)
    plt.title("y Velocity")
    plt.subplot(323)
    plt.plot(x_list, y_list)
    plt.title("x vs y")
    plt.show()

    # print(x_list[-1])
    return t2_list, y_list, x_list


t1, y1, x1 = catapult()
print(f"Distance achieved: {x1[-2]}")

t2, y2, x2 = catapult(R=10.5)
print(f"Distance achieved: {x2[-2]}")

# -----------------------------------------------------------------------------------------
# Game part
pg.init()
pg.display.set_caption("Cow-tapult")
# Files
background = pg.image.load("./Data/Cowtapult/background.jpg")
arthurandmen = pg.image.load("./Data/Cowtapult/arthurandmen.png")
cow = pg.image.load("./Data/Cowtapult/cow.png")

# Window
x_max = 1000
y_max = 600
reso = (x_max, y_max)
scr = pg.display.set_mode(reso)
scrrect = scr.get_rect()

# Background
scr.fill((0, 0, 0))
back_img = pg.transform.scale(background, reso)
back_img = pg.transform.flip(back_img, True, False)
scr.blit(back_img, (0, 0))

# Cow
cowimg = pg.transform.scale(cow, (50, 50))
cowrect = cowimg.get_rect()
x_cow = 300
y_cow = 120
cowrect.centerx = x_cow
cowrect.centery = y_cow
scr.blit(cowimg, cowrect)

# Arthur
arthurimg = pg.transform.scale(arthurandmen, (120, 90))
arthurrect = arthurimg.get_rect()
arthurrect.center = (800, 460)
scr.blit(arthurimg, arthurrect)

pg.display.flip()

# Variables
angle = math.pi / 3

# Text
font = pygame.font.Font('freesansbold.ttf', 50)

# Running
running = True
while running:

    # Keys
    pg.event.pump()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False
    if keys[pg.K_LEFT]:
        if angle >= 0:
            angle -= 0.0005
            angle_ = round(angle * 180 / math.pi, 1)

            text = font.render(f"{str(angle_)}°", True, (255, 0, 0))
            textRect = text.get_rect()
            textRect.center = (300, 400)

            scr.blit(back_img, (0, 0))
            scr.blit(cowimg, cowrect)
            scr.blit(text, textRect)
            scr.blit(arthurimg, arthurrect)
            pg.display.flip()
    if keys[pg.K_RIGHT]:
        t3, y3, x3 = catapult(theta_start=angle)
        for i, j in zip(x3, y3):
            if keys[pg.K_ESCAPE]:
                running = False
            # Change x
            x_cow = int(i * x_max / 500) + 300
            # Change y
            y_cow = y_max - int(j * y_max / 100) - 120

            cowrect.centery = y_cow
            cowrect.centerx = x_cow

            scr.blit(back_img, (0, 0))
            scr.blit(arthurimg, arthurrect)
            scr.blit(cowimg, cowrect)

            pygame.display.flip()
            pg.time.delay(2)

        if 750 < x_cow < 850:
            win = font.render(f"You defeated Arthur!!", True, (255, 0, 0))
            winRect = win.get_rect()
            winRect.center = (300, 400)

            scr.blit(back_img, (0, 0))
            scr.blit(win, winRect)
            scr.blit(arthurimg, arthurrect)
            scr.blit(cowimg, cowrect)

            pygame.display.flip()
        pg.time.delay(2000)
        running = False

pg.quit()
