"""
	Author - Devesh
	Created using MANIM and NETWORKX 
"""

from manimlib.imports import *
import networkx as nx
import manimnx.manimnx as mnx
import numpy as np
import random
import os


# Testing purposes ----
class Test(Scene):
	def construct(self):
		pass

class AddingText(Scene):
	def construct(self):
		first_line = TextMobject("Track and Trace COVID - (TraCov)")
		second_line = TextMobject("- Devesh and Ankur (Team Turing)")
		final_line = TextMobject("Hope you like it! We've worked really hard.", color=BLUE)
		color_final_line = TextMobject("Hack Gujarat 2020 Submission")

		#Coloring
		color_final_line.set_color_by_gradient(BLUE,PURPLE)

		#Position text
		second_line.next_to(first_line, DOWN)

		#Showing text
		self.wait(1)
		self.play(Write(first_line), Write(second_line))
		self.wait(1)
		self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
		self.wait(1)
		self.play(Transform(final_line, color_final_line))
		self.wait(2)

		# Fade OUT
		self.play(FadeOut(color_final_line))
		self.play(FadeOut(final_line))

class AddingNodes(Scene):
	def construct(self):
		
		curr_node = Circle(radius=0.5, color=GREEN, arc_center=ORIGIN+LEFT*2)
		u1_node = Circle(radius=0.5, color=GREEN, arc_center=ORIGIN+UP*2+RIGHT)
		# Current user
		curr_node_name = Text("User", color = WHITE, font='Roberto')
		curr_node_name.move_to(ORIGIN+LEFT*2+DOWN)
		curr_node_name.scale(0.70)

		# 1st Phase
		curr_node.set_fill(GREEN, opacity=1)
		self.add(curr_node)
		self.play(DrawBorderThenFill(curr_node))
		# Add name to the current node
		self.play(Write(curr_node_name))

		end_point = ORIGIN+RIGHT*2
		textAnim = ApplyMethod(curr_node_name.shift, end_point) # Move text with user
		animation = ApplyMethod(curr_node.shift, end_point)
		self.play(animation, textAnim, run_time=4)

		# 2nd Phase
		u1_node.set_fill(GREEN, opacity=1)
		self.add(u1_node)
		#self.play(DrawBorderThenFill(u1_node))
		self.play(ShowCreation(u1_node), run_time=1)
		
		# Add 2 secs wait time before closing
		self.wait(1)
		link1 = ArcBetweenPoints(ORIGIN, ORIGIN+UP*2+RIGHT, run_time=2)
		link2 = ArcBetweenPoints(ORIGIN+UP*2+RIGHT, ORIGIN, run_time=2)

		self.play(ShowCreation(link1))
		self.play(ShowCreation(link2))
		self.wait(1)

		# Now fade them out at the same TIME
		self.play(FadeOut(link1), FadeOut(link2))
		self.wait(1)
		
		comm = Text(" - Unique ID \n - GPS Location \n - Time", font='Roberto')
		# Now form a edge
		edge = Line(ORIGIN, ORIGIN+UP*2+RIGHT, color=GREEN)
		self.add(edge)
		comm.next_to(edge)
		self.play(ShowCreation(edge))
		self.wait(1)
		self.play(Write(comm))
		self.wait(3)
		self.play(FadeOut(comm))


		# Create a phone layout (LOGGING START HERE)
		log = Rectangle(height = 4, width = 2).shift(ORIGIN + RIGHT*4)
		self.play(ShowCreation(log))
		self.wait(3)

		# Move about
		log1 = Text("ID1 | Loc1 | T1", font='Roberto')
		log1.scale(0.40)
		self.add(log1)
		self.play(Write(log1))

		log1.generate_target()
		log1.target.shift(ORIGIN+RIGHT*4-DOWN)
		self.play(MoveToTarget(log1))
		self.wait(1)

		# Now move this whole graph to left
		move = LEFT
		a1 = ApplyMethod(curr_node.shift, move)
		a2 = ApplyMethod(u1_node.shift, move)
		a3 = ApplyMethod(edge.shift, move)
		a4 = ApplyMethod(curr_node_name.shift, move)

		self.play(a1, a2, a3, a4)

		u2Pos = [-3, -2, 0]
		u3Pos = [-5, -3, 0]

		u2_node = Circle(radius=0.5, color=GREEN, arc_center=u2Pos)
		u3_node = Circle(radius=0.5, color=GREEN, arc_center=u3Pos)
		
		# DEBUG PURPOSES
		print(ORIGIN, LEFT, RIGHT, UP, DOWN, UL, UR)
		
		edge1 = Line(u2Pos, u3Pos, color=GREEN)
		self.add(u2_node)
		self.add(u3_node)
		self.add(edge1)
		
		u2_node.set_fill(GREEN, opacity=1)
		u3_node.set_fill(GREEN, opacity=1)

		self.play(ShowCreation(u2_node), ShowCreation(u3_node), ShowCreation(edge1), run_time=0.001)
		self.wait(3)

		# create 3rd edge from two diffrent component
		p1 = ORIGIN + LEFT
		p2 = [-3, -2, 0]

		link1 = ArcBetweenPoints(p1, p2, run_time=2, color=WHITE)
		link2 = ArcBetweenPoints(p2, p1, run_time=2, color=WHITE)
		self.wait(1)

		self.play(ShowCreation(link1))
		self.play(ShowCreation(link2))

		# Now fade them out
		self.play(FadeOut(link1), FadeOut(link2))
		self.wait(1)

		edge2 = Line(p1, p2, color=GREEN)
		self.add(edge2)

		self.play(ShowCreation(edge2))
		self.wait(3)

		# Move about
		log2 = Text("ID2 | Loc2 | T2", font='Roberto')
		log2.scale(0.40)
		self.add(log2)
		self.play(Write(log2))

		log2.generate_target()
		log2.target.shift(ORIGIN+RIGHT*4)
		self.play(MoveToTarget(log2))

		logRecord = Text(" **Logs are recorded over 2 weeks **", font='Roberto')
		logRecord.scale(0.60)
		self.add(logRecord)
		logRecord.shift(DOWN*3.5)
		self.play(Write(logRecord))
		self.wait(3)
		self.play(FadeOut(logRecord))
		self.wait(3)

		self.play(FadeOut(log1))
		self.play(FadeOut(log2))
		self.play(FadeOut(log))
		self.play(FadeOut(logRecord))


		line = TextMobject("Now imagine someone you met earlier gets infected...")
		#Showing text
		self.wait(1)
		line.shift(ORIGIN+3*UP)
		self.play(AddTextWordByWord(line, run_time=5.0))

		edge3 = Line(p1, p1+3*LEFT, color=GREEN)
		self.add(edge3)

		self.play(ShowCreation(edge3))
		self.wait(2)

		extra = Circle(radius=0.5, color=GREEN, arc_center=ORIGIN+LEFT*4)
		extra.set_fill(GREEN, opacity=1)
		self.add(extra)
		self.play(DrawBorderThenFill(extra), run_time=0.5)

		edge4 = Line(p2, p1+3*LEFT, color=GREEN)
		self.add(edge4)
		self.play(ShowCreation(edge4))

		self.wait(2)

		self.play(FadeToColor(extra, RED))

		self.wait(2)
		self.play(FadeOut(line))
		self.wait(1)
		line = TextMobject("Every direct connected edge gets notified about the infected user")
		#Showing text
		self.wait(1)
		line.shift(ORIGIN+3*UP)
		kline = TextMobject("and is put into POTENTIAL THREAT class")
		kline.next_to(line, DOWN)

		self.play(Write(kline), Write(line))
		self.wait(1)

		self.play(AddTextWordByWord(line, run_time=5.0))

		self.play(FadeToColor(edge3, RED))
		self.wait(1)
		self.play(FadeToColor(edge4, RED))
		self.wait(2)

		self.play(FadeToColor(curr_node, RED))
		self.play(FadeToColor(u2_node, RED))
		self.wait(3)

		# COLOR NODES - RED






