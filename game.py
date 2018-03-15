import pygame
import random
import sys

# @desc Container that holds everything else of the program
# 
# @param none
# @return void
def main():
	pygame.init()
	game_continue = 1
	score = [0]	
	screen_width = 700
	screen_height = 400

	screen = pygame.display.set_mode([screen_width,screen_height])
	screen.fill((0, 0, 0))

	while game_continue is 1:
		TitleScreen(screen, screen_width, screen_height)
		PlayGame(screen, screen_width, screen_height, score)

		game_continue = GameOver(screen, screen_width, screen_height, score)

	return

def PlayGame(screen, screen_width, screen_height, score):
	myfont = pygame.font.SysFont("monospace", 25)
	screen.fill((0,0,0))
	pygame.display.update()
	proj = []
	p = Player()
	score[0] = 0

	i = 0
	j = 0
	score_counter = 0
	game_continue = True
	while game_continue:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()

		screen.fill((0, 0, 0))
		p.Update(screen, keys, screen_height, screen_width)

		if(random.randrange(0, 100) > 90 - score[0] * 0.03):	
			proj.append(Projectile(screen_width, screen_height, (score[0] * 0.04 + 5)))

		if len(proj) is not 0:
			for projectile in proj:
				if projectile.x + projectile.w < 0:
					proj.remove(projectile)
				else:
					projectile.Update(screen)
					if projectile.x < p.x + p.w and projectile.x + projectile.w > p.x and projectile.y < p.y + p.h and projectile.h + projectile.y > p.y:
						game_continue = False

		scoretext = myfont.render("Score = "+str(score[0]), 1, (255,255,255))
		screen.blit(scoretext, (5, 10))
		pygame.display.update()

		if score_counter == 0:
			score[0] += 1
			score_counter = 10
		else:
			score_counter -= 1
	return


def GameOver(screen, screen_width, screen_height, score):

	gameover = pygame.font.SysFont("monospace", 40)
	endscore = pygame.font.SysFont("monospace", 30)
	decision = pygame.font.SysFont("monospace", 25)

	i = 40
	while(True):

		screen.fill((0, 0, 0))

		gameOverText = gameover.render("GAME OVER", 1, (255,255,255))
		screen.blit(gameOverText, (screen_width/2 - 80, screen_height/2 - 50))

		scoretext = endscore.render("Score = "+str(score[0]), 1, (255,255,255))
		screen.blit(scoretext, (screen_width/2-45, screen_height/2 - 15))

		if i <= 40:
			decisionText = decision.render("> Press 'e' to exit()", 1, (255,255,255))
			screen.blit(decisionText, (10, screen_height/2+10))

			decisionText = decision.render("> Press spacebar to play again()", 1, (255,255,255))
			screen.blit(decisionText, (10, screen_height/2+30))

			if i == 0:
				i = 80
			else:
				i -= 1

		elif i > 40:
			i -= 1

		pygame.display.update()
		keys = pygame.key.get_pressed()

		if keys[pygame.K_SPACE]:
			return 1
		elif keys[pygame.K_e]:
			return 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()

def TitleScreen(screen, screen_width, screen_height):
	proj = []
	screen.fill((0,0,0))
	Title = pygame.font.SysFont("monospace", 80)
	Intr = pygame.font.SysFont("monospace", 40)
	pygame.display.update()

	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()

		if keys[pygame.K_SPACE]:
			break
		screen.fill((0, 0, 0))
		if(random.randrange(0, 100) > 90):	
			proj.append(Projectile(screen_width, screen_height, 5))
		if len(proj) is not 0:
			for projectile in proj:
				if projectile.x + projectile.w < 0:
					proj.remove(projectile)
				else:
					projectile.Update(screen)
		TitleText = Title.render("Dodger", 1, (255,255,255))
		InstrText = Intr.render("Press Space to Play()", 1, (255,255,255))
		screen.blit(TitleText, (screen_width/2 - 100, screen_height/4))
		screen.blit(InstrText, (screen_width/2 - 150, screen_height/2))

		pygame.display.update()

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
		pygame.draw.rect(screen, (10, 10, 255), (self.x, self.y, self.w, self.h), 0)

	def UpdatePos(self):
		self.x -= self.v

main()
