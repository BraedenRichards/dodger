import pygame
import random
import sys

# @desc Container that holds everything else of the program
# 
# @param none
# @return void
def main():
	pygame.init()
	p = Player()
	game_continue = True
	score = 0
	myfont = pygame.font.SysFont("monospace", 16)
	gameover = pygame.font.SysFont("monospace", 40)
	endscore = pygame.font.SysFont("monospace", 30)
	
	screen_width = 700
	screen_height = 400

	screen = pygame.display.set_mode([screen_width,screen_height])
	screen.fill((255, 255, 255))

	screen.fill((255,255,255))
	pygame.display.update()
	proj = []

	i = 0
	j = 0
	score_counter = 0
	while game_continue:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()

		screen.fill((255, 255, 255))
		p.Update(screen, keys, screen_height, screen_width)

		# if j == 0:
		# 	proj.append(Projectile(screen_width, screen_height, (score * 0.04 + 5)))
		# 	j = 8
		# else:
		# 	j -= 1
		if(random.randrange(0, 100) > 90 - score * 0.03):	
			proj.append(Projectile(screen_width, screen_height, (score * 0.04 + 5)))

		if len(proj) is not 0:
			for projectile in proj:
				if projectile.x + projectile.w < 0:
					proj.remove(projectile)
				else:
					projectile.Update(screen)
					if projectile.x < p.x + p.w and projectile.x + projectile.w > p.x and projectile.y < p.y + p.h and projectile.h + projectile.y > p.y:
						game_continue = False

		scoretext = myfont.render("Score = "+str(score), 1, (0,0,0))
		screen.blit(scoretext, (5, 10))
		pygame.display.update()

		if score_counter == 0:
			score += 1
			score_counter = 10
		else:
			score_counter -= 1

	while(True):
		screen.fill((0, 0, 0))

		gameOverText = gameover.render("GAME OVER", 1, (255,255,255))
		screen.blit(gameOverText, (screen_width/2 - 80, screen_height/2 - 50))

		scoretext = endscore.render("Score = "+str(score), 1, (255,255,255))
		screen.blit(scoretext, (screen_width/2-45, screen_height/2 - 15))

		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()

	return



class Player:
	def __init__(self):
		self.x = 100
		self.y = 100
		self.w = 25
		self.h = 25

	def Update(self, screen, keys, screen_height, screen_width):
		self.UpdatePos(keys, screen_height, screen_width)
		self.ShowPlayer(screen)

	def ShowPlayer(self, screen):
		pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.w, self.h), 3)

	def UpdatePos(self, keys, screen_height, screen_width):
		if keys[pygame.K_UP]:
			if self.y > 0:
				self.y -= 6
		elif keys[pygame.K_DOWN]:
			if (self.y + self.h) < screen_height:
				self.y += 6
		if keys[pygame.K_LEFT]:
			if self.x > 0:
				self.x -= 6
		elif keys[pygame.K_RIGHT]:
			if (self.x + self.w) < screen_width:
				self.x += 6

class Projectile:
	def __init__(self, width, height, v):
		self.x = width - 1
		self.y = random.randrange(0, height - 30)
		self.h = 30
		self.w = 30
		self.v = v

	def Update(self, screen):
		self.UpdatePos()
		self.ShowProjectile(screen)

	def ShowProjectile(self, screen):
		pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.w, self.h), 0)

	def UpdatePos(self):
		self.x -= self.v

main()