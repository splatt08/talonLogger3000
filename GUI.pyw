#! c:\\Users\\ipfa1\\AppData\\Local\\Programs\\Python\\Python310\\pythonw.exe
from talonLogger3000 import logger3000
import csv
import nfc
from nfc.clf import RemoteTarget
import pygame
import time
pygame.init()

#grab logon data from csv
with open('logonList.csv', newline='') as logonList:
    for ac in csv.reader(logonList):
            logged_on_users = ac
#print("heyo test at call" + str(logged_on_users))


# initialize nfc scanner
clf = nfc.ContactlessFrontend()
assert clf.open('tty:USB0:pn532') is True 
target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))

#setup pygame window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Talon Logger 3000')
screen.fill((227, 227, 227))
image = pygame.image.load(r'assets/TalonLoggerLogo.png')
image_rect = image.get_rect ()
image_rect.center = (screen.get_width()/2, 0 + 100)
font = pygame.font.Font(r'assets/ValorantFont.ttf', 32)
admin_font = pygame.font.Font(r'assets/ValorantFont.ttf', 42)
login_font = pygame.font.Font(r'assets/ValorantFont.ttf', 42)




running = True
while running:
    # Did the user click the window close button?
    screen.blit(image, (image_rect.left, image_rect.top))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    text = login_font.render('Please Tap Card', True, (0, 255, 0), (0, 0, 128))
    textRect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    
    screen.blit(text, textRect)
    pygame.display.update()

    # Grab values from scanner
    #print("heyo test at before func call" + str(logged_on_users))
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
    #print(tag)
    scan_num = str(tag)
    #print(tag)
    scan_num = scan_num[12:]
    

    #print(scan_num)
    #quit = input(quit)
    #print("heyo test after func call" + str(logged_on_users))
    logger_data = logger3000(scan_num, logged_on_users)
    logged_on_users = logger_data[5]
    screen.fill((227, 227, 227))
    screen.blit(image, (image_rect.left, image_rect.top))



    if logger_data[1] == 'AAF5CF23':

        screen.fill((227, 227, 227))
        admin_text = admin_font.render('Admin Panel', True, (0, 0, 0), (227, 227, 227))
        admin_text_rect = admin_text.get_rect(center=(screen.get_width()/2, 100))
        screen.blit(admin_text, admin_text_rect)
        settings_button = font.render('Settings', True, (0, 0, 0), (227, 227, 227))
        settings_button_rect = settings_button.get_rect(center=(screen.get_width()/2, screen.get_height()/2-100))
        screen.blit(settings_button, settings_button_rect)
        manual_login = font.render('Manual Login', True, (0, 0, 0), (227, 227, 227))
        manual_login_rect = manual_login.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(manual_login, manual_login_rect)
        back_button = font.render('Back', True, (0, 0, 0), (227, 227, 227))
        back_button_rect = back_button.get_rect(center=(screen.get_width()/2, screen.get_height()/2+100))
        screen.blit(back_button, back_button_rect)
        quit_button = font.render('Quit', True, (0, 0, 0), (227, 227, 227))
        quit_button_rect = quit_button.get_rect(center=(screen.get_width()/2, screen.get_height()/2+200))
        screen.blit(quit_button, quit_button_rect)
        running_inside = True

        while running_inside:
            for ev in pygame.event.get():
                if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    quit_button = font.render('Quit', True, (100, 100, 100), (227, 227, 227))
                    screen.blit(quit_button, quit_button_rect)
                    if quit_button_rect.collidepoint(pygame.mouse.get_pos()) & (ev.type == pygame.MOUSEBUTTONDOWN):
                        pygame.quit()
                        clf.close()
                        quit()
                else:
                    quit_button = font.render('Quit', True, (0, 0, 0), (227, 227, 227))
                    screen.blit(quit_button, quit_button_rect)
                


                if manual_login_rect.collidepoint(pygame.mouse.get_pos()):
                    manual_login = font.render('Manual Login', True, (100, 100, 100), (227, 227, 227))
                    screen.blit(manual_login, manual_login_rect)

                    if manual_login_rect.collidepoint(pygame.mouse.get_pos()) & (ev.type == pygame.MOUSEBUTTONDOWN):
                        screen.fill((227, 227, 227))
                        running_inside_inside = True
                        cancel_button = font.render('Cancel', True, (0, 0, 0), (227, 227, 227))
                        cancel_button_rect = cancel_button.get_rect(center=(screen.get_width()/2, screen.get_height()/2+200))
                        screen.blit(cancel_button, cancel_button_rect)
                        manual_text = admin_font.render('Manual Login', True, (0, 0, 0), (227, 227, 227))
                        manual_text_rect = admin_text.get_rect(center=(screen.get_width()/2, 100))
                        screen.blit(manual_text, manual_text_rect)
                        info = "Start Typing"
                        block_a = font.render(info, True, (255, 255, 255))
                        rect_a = block_a.get_rect()
                        rect_a.center = screen.get_rect().center
                        screen.blit(block_a, rect_a)
                        name = ""


                        while running_inside_inside:
                            manual_text = admin_font.render('Manual Login', True, (0, 0, 0), (227, 227, 227))
                            manual_text_rect = admin_text.get_rect(center=(screen.get_width()/2, 100))
                            screen.blit(manual_text, manual_text_rect)
                            for ev in pygame.event.get():

                                if cancel_button_rect.collidepoint(pygame.mouse.get_pos()):

                                    cancel_button = font.render('Cancel', True, (100, 100, 100), (227, 227, 227))
                                    screen.blit(cancel_button, cancel_button_rect)

                                    if cancel_button_rect.collidepoint(pygame.mouse.get_pos()) & (ev.type == pygame.MOUSEBUTTONDOWN):
                                        screen.fill((227, 227, 227))
                                        running_inside_inside = False
                                        running_inside = False
                                        continue
                                        

                                else:
                                    cancel_button = font.render('Cancel', True, (0, 0, 0), (227, 227, 227))
                                    screen.blit(cancel_button, cancel_button_rect)
                                
                                if ev.type == pygame.KEYDOWN:
                                    if ev.unicode.isalpha():
                                        name += ev.unicode
                                    elif ev.key == pygame.K_BACKSPACE:
                                        name = name[:-1]
                                    elif ev.key == pygame.K_RETURN:
                                        with open('users.csv', newline='') as users_csv:
                                            user_read = csv.reader(users_csv)
                                            for row in user_read:
                                            
                                                if row[0] == name:
                                                    scan_num = row[1]
                                            logger_data = logger3000(scan_num, logged_on_users)
                                            running_inside_inside = False
                                            running_inside = False
                                            continue

                                    
                                    screen.fill((227, 227, 227))
                                    block = font.render(name, True, (255, 255, 255))
                                    rect = block.get_rect()
                                    rect.center = screen.get_rect().center
                                    screen.blit(block, rect)
                                    pygame.display.flip()
                            pygame.display.update()
                        else:
                            break

                        
                else:
                    manual_login = font.render('Manual Login', True, (0, 0, 0), (227, 227, 227))
                    screen.blit(manual_login, manual_login_rect)
                
                if back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    back_button = font.render('Back', True, (100, 100, 100), (227, 227, 227))
                    screen.blit(back_button, back_button_rect)
                    if back_button_rect.collidepoint(pygame.mouse.get_pos()) & (ev.type == pygame.MOUSEBUTTONDOWN):
                        screen.fill((227, 227, 227))
                        running_inside = False
                        break
                else:
                    back_button = font.render('Back', True, (0, 0, 0), (227, 227, 227))
                    screen.blit(back_button, back_button_rect)

                if settings_button_rect.collidepoint(pygame.mouse.get_pos()):
                    settings_button = font.render('Settings', True, (100, 100, 100), (227, 227, 227))
                    screen.blit(settings_button, settings_button_rect)
                    if settings_button_rect.collidepoint(pygame.mouse.get_pos()) & (ev.type == pygame.MOUSEBUTTONDOWN):
                        screen.fill((227, 227, 227))
                        running_inside_inside = True
                        done_button = font.render('Done', True, (0, 0, 0), (227, 227, 227))
                        done_button_rect = done_button.get_rect(center=(screen.get_width()/2, screen.get_height()/2+200))
                        screen.blit(done_button, done_button_rect)
                        settings_text = admin_font.render('Settings', True, (0, 0, 0), (227, 227, 227))
                        settings_text_rect = settings_text.get_rect(center=(screen.get_width()/2, 100))
                        screen.blit(settings_text, settings_text_rect)
                        name = ""


                        while running_inside_inside:
                            
                            for ev in pygame.event.get():

                                if done_button_rect.collidepoint(pygame.mouse.get_pos()):

                                    done_button = font.render('Done', True, (100, 100, 100), (227, 227, 227))
                                    screen.blit(done_button, done_button_rect)

                                    if done_button_rect.collidepoint(pygame.mouse.get_pos()) & (ev.type == pygame.MOUSEBUTTONDOWN):
                                        screen.fill((227, 227, 227))
                                        running_inside_inside = False
                                        running_inside = False
                                        continue
                                        

                                else:
                                    done_button = font.render('Done', True, (0, 0, 0), (227, 227, 227))
                                    screen.blit(done_button, done_button_rect)
                            pygame.display.update()
                else:
                    settings_button = font.render('Settings', True, (0, 0, 0), (227, 227, 227))
                    screen.blit(settings_button, settings_button_rect)
                

            pygame.display.update()
    


    screen.fill((227, 227, 227))
    screen.blit(image, (image_rect.left, image_rect.top))

    if logger_data[1] != 'null':
        
        if logger_data[4] == "True":
            print(logger_data[0] +  ' has been logged in')
            logged_in_text = admin_font.render(logger_data[0] +  ' has been logged in', True, (0, 255, 0), (0, 0, 128))
            logged_in_text_rect = logged_in_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
            screen.blit(logged_in_text, logged_in_text_rect)
        
        else:
            print(logger_data[0] + ' has been logged out')
            logged_out_text = admin_font.render(logger_data[0] +  ' has been logged out', True, (0, 255, 0), (0, 0, 128))
            logged_out_text_rect = logged_out_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
            screen.blit(logged_out_text, logged_out_text_rect)
    
    else:
        print('ERROR!')
        error_text = admin_font.render(logger_data[0] +  ' has been logged out', True, (0, 255, 0), (0, 0, 128))
        error_text_rect = error_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(error_text, error_text_rect)
    pygame.display.update()
    time.sleep(2) 
    screen.fill((227, 227, 227))

clf.close()
pygame.quit()