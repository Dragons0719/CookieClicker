import pygame
import math

pygame.init()

cookies = 0
cps = 0
click_weight = 1
animating = False
animation_frames = 10
animation_counter = 0
cursor_price = 10
cursor_owned = 0
grandma_owned = 0
bakery_owned = 0
factory_owned = 0
mine_owned = 0
reactor_owned = 0
grandma_price = 100
bakery_price = 1000
factory_price = 10000
mine_price = 100000
reactor_price = 1000000
icon_image = pygame.image.load('Pictures\Cookie_icon.ico')
pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode([1500, 843.75])
pygame.display.set_caption('Cookie Clicker')
BACKGROUND_IMG = pygame.image.load("Pictures/Background.png").convert()
COOKIE_IMG = pygame.image.load("Pictures/Cookie.png").convert_alpha()
COOKIE = pygame.transform.scale(COOKIE_IMG, (400, 400))
cookie_rect = COOKIE.get_rect(topleft=(214, 245))
rectangle_surface = pygame.Surface((636, 100), pygame.SRCALPHA)
rect_color = (0, 0, 0, 175)  # Transparent black
pygame.draw.rect(rectangle_surface, rect_color, rectangle_surface.get_rect())
rectangle_surface2 = pygame.Surface((900, 843.75), pygame.SRCALPHA)
rect_color2 = (0, 0, 0, 175)  # Transparent black
pygame.draw.rect(rectangle_surface2, rect_color2, rectangle_surface2.get_rect())
font_path = "Other Resources/Patrick_Hand/PatrickHand-Regular.ttf"
font_size = 65
font_size2 = 30
font = pygame.font.Font(font_path, font_size)
font2 = pygame.font.Font(font_path, font_size2)
white_color = (255, 255, 255)
button_width = 550
button_height = 130
button_color = (100, 100, 100, 175)
CURSOR_IMG = pygame.image.load("Pictures/cursor.png").convert_alpha()
CURSOR_IMG = pygame.transform.scale(CURSOR_IMG, (80, 80))
GRANDMA_IMG = pygame.image.load("Pictures/grandma.png").convert_alpha()
BAKERY_IMG = pygame.image.load("Pictures/bakery.png").convert_alpha()
FACTORY_IMG = pygame.image.load("Pictures/factory.png").convert_alpha()
MINE_IMG = pygame.image.load("Pictures/mine.png").convert_alpha()
REACTOR_IMG = pygame.image.load("Pictures/reactor.png").convert_alpha()
buttons = []
button_images = [CURSOR_IMG, GRANDMA_IMG, BAKERY_IMG, FACTORY_IMG, MINE_IMG, REACTOR_IMG]
button_texts = ["Cursor", "Grandma", "Bakery", "Factory", "Mine", "Cooklier Reactor"]
button_texts2 = [f"Amount Owned: {cursor_owned}", f"Amount Owned: {grandma_owned}", f"Amount Owned: {bakery_owned}", f"Amount Owned: {factory_owned}", f"Amount Owned: {mine_owned}", f"Amount Owned: {reactor_owned}"]
button_texts3 = [f"Price: {cursor_price}", f"Price: {grandma_price}", f"Price: {bakery_price}", f"Price: {factory_price}", f"Price: {mine_price}", f"Price: {reactor_price}"]
button_font = pygame.font.Font(font_path, 40)
button_font2 = pygame.font.Font(font_path, 25) 
button_font3 = pygame.font.Font(font_path, 20)  
max_button_width = 500  
max_button_height = 100 
button_colors = [(100, 100, 100, 175)] * len(button_texts) 

for i, text in enumerate(button_texts):
    button_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
    price = [cursor_price, grandma_price, bakery_price, factory_price, mine_price, reactor_price][i]
    pygame.draw.rect(button_surface, button_colors[i], button_surface.get_rect())
    original_image = button_images[i]
    image_aspect_ratio = original_image.get_width() / original_image.get_height()
    scaled_width = min(original_image.get_width(), max_button_width)
    scaled_height = min(original_image.get_height(), max_button_height)
    scaled_width = min(scaled_width, int(scaled_height * image_aspect_ratio))
    scaled_height = int(scaled_width / image_aspect_ratio)
    image_x_pos = 20
    if text in ["Bakery", "Factory", "Mine"]:
        image_x_pos -= 10 
    
    button_surface.blit(pygame.transform.scale(original_image, (scaled_width, scaled_height)), (image_x_pos, (button_height - scaled_height) // 2))
    button_text = button_font.render(text, True, white_color)
    button_text2 = button_font2.render(button_texts2[i], True, white_color)
    button_text3 = button_font3.render(button_texts3[i], True, white_color)
    button_surface.blit(button_text, (120, 10)) 
    button_surface.blit(button_text2, (120, 65)) 
    button_surface.blit(button_text3, (120, 95)) 
    
    buttons.append(button_surface)

num_buttons = 6
total_height = 843.75
spacing = (total_height - (num_buttons * button_height)) / (num_buttons + 1)
x_coordinate = 895 
button_positions = [(x_coordinate, spacing + i * (button_height + spacing)) for i in range(num_buttons)]
last_update_time = pygame.time.get_ticks()
cps_interval = 1000 
running = True

while running:
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - last_update_time

    if elapsed_time >= cps_interval:
        cookies += round(cps, 1)
        last_update_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cookie_rect.collidepoint(event.pos) and not animating:
                cookies += 1
                animating = True
                animation_counter = 0
            if event.button == 1:
                for i, pos in enumerate(button_positions):
                    button_rect = pygame.Rect(pos[0], pos[1], button_width, button_height)
                    if button_rect.collidepoint(event.pos):
                        if i == 0: 
                            if cookies >= cursor_price:
                                cursor_owned += 1
                                cookies -= cursor_price
                                cursor_price = int((cursor_price * 0.17) + cursor_price) 
                                cps += 1
                                button_texts2[i] = f"Amount Owned: {cursor_owned}" 
                                button_texts3[i] = f"Price: {cursor_price}" 
                                break
                        if i == 1:
                            if cookies >= grandma_price:
                                grandma_owned += 1
                                cookies -= grandma_price
                                grandma_price = int((grandma_price * 0.17) + grandma_price)
                                cps += 10
                                button_texts2[i] = f"Amount Owned: {grandma_owned}" 
                                button_texts3[i] = f"Price: {grandma_price}" 
                                break
                        if i == 2:
                            if cookies >= bakery_price:
                                bakery_owned += 1
                                cookies -= bakery_price
                                bakery_price = int((bakery_price * 0.17) + bakery_price)
                                cps += 100
                                button_texts2[i] = f"Amount Owned: {bakery_owned}" 
                                button_texts3[i] = f"Price: {bakery_price}" 
                                break
                        if i == 3:
                            if cookies >= factory_price:
                                factory_owned += 1
                                cookies -= factory_price
                                factory_price = int((factory_price * 0.17) + factory_price)
                                cps += 1000
                                button_texts2[i] = f"Amount Owned: {factory_owned}" 
                                button_texts3[i] = f"Price: {factory_price}" 
                                break
                        if i == 4:
                            if cookies >= mine_price:
                                mine_owned += 1
                                cookies -= mine_price
                                mine_price = int((mine_price * 0.17) + mine_price)
                                cps += 10000
                                button_texts2[i] = f"Amount Owned: {mine_owned}" 
                                button_texts3[i] = f"Price: {mine_price}"  
                                break
                        if i == 5:
                            if cookies >= reactor_price:
                                reactor_owned += 1
                                cookies -= reactor_price
                                reactor_price = int((reactor_price * 0.17) + reactor_price)
                                cps += 100000
                                button_texts2[i] = f"Amount Owned: {reactor_owned}"  
                                button_texts3[i] = f"Price: {reactor_price}" 
                                break
    screen.blit(BACKGROUND_IMG, (0, 0))

    if animating:
        progress = animation_counter / animation_frames
        if progress < 0.5:
            scale_factor = 1 - 0.2 * math.sin(progress * math.pi)
        else:
            scale_factor = 0.8 + 0.2 * math.sin((progress - 0.5) * math.pi)

        animation_counter += 1
        if animation_counter >= animation_frames:
            animating = False

        scaled_cookie = pygame.transform.scale(COOKIE_IMG, (int(415 * scale_factor), int(415 * scale_factor)))
        scaled_cookie_rect = scaled_cookie.get_rect(center=cookie_rect.center)
        screen.blit(scaled_cookie, scaled_cookie_rect.topleft)
    else:
        screen.blit(COOKIE, cookie_rect.topleft)

    screen.blit(rectangle_surface, (98, 20))
    screen.blit(rectangle_surface2, (845, 0))  
    button_prices = [cursor_price, grandma_price, bakery_price, factory_price, mine_price, reactor_price]
    for i, pos in enumerate(button_positions):
        if cookies >= button_prices[i]:
            button_colors[i] = (0, 255, 0, 175)  
        else:
            button_colors[i] = (100, 100, 100, 175)  
        button_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, button_colors[i], button_surface.get_rect())
        
        original_image = button_images[i]
        image_aspect_ratio = original_image.get_width() / original_image.get_height()
        scaled_width = min(original_image.get_width(), max_button_width)
        scaled_height = min(original_image.get_height(), max_button_height)
        scaled_width = min(scaled_width, int(scaled_height * image_aspect_ratio))
        scaled_height = int(scaled_width / image_aspect_ratio)
        image_x_pos = 20
        if button_texts[i] in ["Bakery", "Factory", "Mine"]:
            image_x_pos -= 10
        button_surface.blit(pygame.transform.scale(original_image, (scaled_width, scaled_height)), (image_x_pos, (button_height - scaled_height) // 2))
        button_text = button_font.render(button_texts[i], True, white_color)
        button_text2 = button_font2.render(button_texts2[i], True, white_color)
        button_text3 = button_font3.render(button_texts3[i], True, white_color)
        button_surface.blit(button_text, (120, 10))
        button_surface.blit(button_text2, (120, 65))
        button_surface.blit(button_text3, (120, 95))
        
        buttons[i] = button_surface
    
    for i, pos in enumerate(button_positions):
        screen.blit(buttons[i], pos)

    text = f"Cookies: {cookies}"
    text_surface = font.render(text, True, white_color)
    screen.blit(text_surface, (295, 10))

    rounded_cps = math.ceil(cps) if math.isclose(cps % 1, 0.9, abs_tol=0.01) else round(cps)
    text2 = f"Passive CPS: {int(rounded_cps)}"
    text_surface2 = font2.render(text2, True, white_color)
    screen.blit(text_surface2, (337, 80))

    pygame.display.flip()

pygame.quit()
