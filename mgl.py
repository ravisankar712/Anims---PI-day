from manimlib.imports import *

class WhatIsPI(Scene):

    def construct(self):
        
        pi = TexMobject("\\pi").scale(8).set_color(YELLOW)
        pi.save_state()
        logo = TextMobject("s","c","i","e","n","c","e",".","s","o","r","t","(",")").scale(3)
        pi.scale(3./8)
        pi.move_to(logo[4])
        self.play(
            Write(logo)
        )
        self.wait()
        self.play(
            ReplacementTransform(logo[4], pi)
        )
        self.wait()
        self.play(
            FadeOut(logo)
        )
        self.play(
            pi.restore
        )
        self.wait()
        self.play(
            ApplyWave(pi)
        )
        self.wait()
        
        self.play(
            ApplyMethod(pi.to_edge, LEFT)
        )
        self.play(
            ApplyMethod(pi.scale, 1./3)
        )

        self.wait()

        center = Dot().shift(RIGHT * 4).set_color("#ffd166")
        radius = Line(LEFT/2, RIGHT/2)
        radius.move_to(center.get_center() + radius.get_length() / 2.0 * RIGHT).set_color("#ffd166")
        circle = Circle(radius=radius.get_length()).move_to(center).set_color("#d62828")

        # self.add(center, radius, circle)

        def trace_circle(mob, alpha):
            mob.restore()
            mob.rotate(alpha * TAU, about_point=center.get_center())

        radius.save_state()

        self.play(
            GrowFromCenter(center)
        )
        self.play(
            GrowArrow(radius)
        )
        self.wait()
        self.play(
            ShowCreation(circle),
            UpdateFromAlphaFunc(radius, trace_circle)
        )


        perimeter = Line(ORIGIN, RIGHT * 2 * PI * radius.get_length()).rotate(PI/2).shift(LEFT * 5).set_color("#d62828")
        brace_p = Brace(perimeter, LEFT)
        p = TextMobject("p").next_to(brace_p, LEFT).scale(2).set_color("#d62828")

        self.wait()
        self.play(
            TransformFromCopy(circle, perimeter)
        )
        self.play(
            GrowFromCenter(brace_p),
            Write(p)
        )
        self.wait()

        r_copy1 = Line(LEFT/2, RIGHT/2).rotate(PI/2).set_color("#ffd166")
        r_copy2 = Line(LEFT/2, RIGHT/2).rotate(PI/2).set_color("#ffd166")

        self.play(
            TransformFromCopy(radius, r_copy1)
        )
        self.add(r_copy2)

        def half_rotate(mob, alpha):
            mob.restore()
            mob.rotate(-PI * alpha, about_point=mob.get_center() + DOWN * mob.get_length() * 0.5)

        r_copy2.save_state()

        self.play(
            UpdateFromAlphaFunc(r_copy2, half_rotate)
        )

        brace_d = Brace(VGroup(r_copy1, r_copy2), LEFT)
        d = TexMobject("d").next_to(brace_d, LEFT).scale(2).set_color("#ffd166")
        
        self.play(
            GrowFromCenter(brace_d),
            Write(d)
        )

        
        eq = TexMobject("=").scale(2).next_to(pi, RIGHT)
        ratio = TexMobject("p", "\\over", "d").scale(2).next_to(eq, RIGHT)
        self.wait()
        self.play(
            FadeOut(brace_d),
            FadeOut(brace_p),
            FadeOut(r_copy1),
            FadeOut(r_copy2),
            FadeOut(perimeter),
            ApplyMethod(p.move_to, ratio[0]),
            ApplyMethod(d.move_to, ratio[2]),
            Write(ratio[1]),
            Write(eq)
        )

        self.play(
            ApplyMethod(pi.shift, RIGHT * 4),
            ApplyMethod(p.shift, RIGHT * 4),
            ApplyMethod(eq.shift, RIGHT * 4),
            ApplyMethod(d.shift, RIGHT * 4),
            ApplyMethod(ratio[1].shift, RIGHT * 4),
        )

       
        self.wait()

class ValueOfPI(Scene):
    def construct(self):
        value = TexMobject("\\pi", "=", "3", "\\cdot", "1", "4", "1", "5", "9", "2", "6", "5", "3", "\\cdots").scale(2.5)
        value[:6].move_to(ORIGIN)
        self.play(
            Write(value[:6])
        )
        self.wait(0.5)
        self.play(
            Indicate(value[2])
        )
        self.play(
            Indicate(value[4:6])
        )
        self.wait(2)
        for i in range(6, len(value), 1):
            value[i].next_to(value[:i], RIGHT)
            self.play(
                Write(value[i]),
                run_time=0.2
            )
            self.play(
                ApplyMethod(value[:i+1].move_to, ORIGIN),
                run_time=0.2
            )
        
        self.wait()

class SeriesIntro(Scene):

    def construct(self):
        series = TexMobject("\\frac{\\pi}{4}", "= ", "1 ", "- ", "\\frac{1}{3}", "+ ", "\\frac{1}{5}", "- ", "\\frac{1}{7}", "+ ", "\\frac{1}{9}", "-",  "\\cdots")

        series.scale(2)
        series.set_color("#90be6d")
        
        self.wait()
        self.play(
            Write(
                series[2]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[3:5]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[5:7]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[7:9]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[9:11]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[11:]
            )
        )
        self.wait(2)
        self.play(
            Write(
                series[:2]
            )
        )

        self.wait()
        
        mgl = TextMobject("Madhava", "-", "Gregory", "-", "Leibniz", " Series").scale(1.5).to_edge(UP).set_color("#f9c74f")
        self.play(
            Write(mgl)
        )
        self.wait()

class SimilarTriangles(Scene):

    def construct(self):
        coord_A = ORIGIN
        coord_B = RIGHT * 1.5
        coord_C = UP * 3
        coord_P = ORIGIN
        coord_Q = UP * 1.5
        coord_R = LEFT * 1.5/2.0

        t_ABC = VGroup(
            Dot().move_to(coord_A),
            Dot().move_to(coord_B),
            Dot().move_to(coord_C),
            Polygon(coord_A, coord_B, coord_C, color="#99d98c")
        ).shift(RIGHT)

        t_PQR = VGroup(
            Dot().move_to(coord_P),
            Dot().move_to(coord_Q),
            Dot().move_to(coord_R),
            Polygon(coord_P, coord_Q, coord_R, color="#99d98c")
        ).shift(LEFT)
        
        self.play(
            ShowCreation(t_ABC)
        )
        A = TexMobject("A").scale(0.7).next_to(t_ABC[0], LEFT)
        B = TexMobject("B").scale(0.7).next_to(t_ABC[1], RIGHT)
        C = TexMobject("C").scale(0.7).next_to(t_ABC[2], UP)

        self.play(
            Write(A),
            Write(B),
            Write(C)
        )

        self.play(
            ShowCreation(t_PQR)
        )
        P = TexMobject("P").scale(0.7).next_to(t_PQR[0], RIGHT)
        Q = TexMobject("Q").scale(0.7).next_to(t_PQR[1], UP)
        R = TexMobject("R").scale(0.7).next_to(t_PQR[2], LEFT)

        self.play(
            Write(P),
            Write(Q),
            Write(R)
        )
        self.wait()

        AeqP = TexMobject("\\angle A", "=", "\\angle P").shift(DOWN + LEFT * 3)
        BeqR = TexMobject("\\angle B", "=", "\\angle R").shift(DOWN)
        CeqQ = TexMobject("\\angle C", "=", "\\angle Q").shift(DOWN + RIGHT * 3)

        self.play(
            Write(AeqP)
        )
        self.play(
            Write(BeqR)
        )
        self.play(
            Write(CeqQ)
        )

        self.wait()
        similarity = TexMobject("\\sim").next_to(t_PQR, RIGHT, buff=1.0)
        self.play(
            ShowCreation(similarity)
        )
        sumis180 = TexMobject("\\angle A + \\angle B + \\angle C", "=", "180^{\\circ}", "=",  "\\angle P + \\angle Q + \\angle R")
        sumis180.shift(DOWN * 2)

        self.wait()
        self.play(
            Write(
                sumis180[0]
            )
        )
        self.play(
            Write(
                sumis180[-1]
            )
        )
        self.play(
            Write(
                sumis180[1:-1]
            )
        )
        self.wait()
        

        self.play(
            AnimationGroup(Indicate(AeqP), Indicate(BeqR), Indicate(CeqQ), lag_ratio=0.6), 
        )

        self.wait()
        self.play(
            Uncreate(sumis180)
        )

        ratio = TexMobject("\\frac{BC}{QR}", "=", "\\frac{AC}{PQ}", "=", "\\frac{AB}{PR}").shift(DOWN * 2)
        line_BC = Line(t_ABC[1], t_ABC[2], stroke_width=8.0).set_color(YELLOW)
        line_QR = Line(t_PQR[1], t_PQR[2], stroke_width=8.0).set_color(YELLOW)
        line_AC = Line(t_ABC[0], t_ABC[2], stroke_width=8.0).set_color(YELLOW)
        line_PQ = Line(t_PQR[0], t_PQR[1], stroke_width=8.0).set_color(YELLOW)
        line_AB = Line(t_ABC[0], t_ABC[1], stroke_width=8.0).set_color(YELLOW)
        line_PR = Line(t_PQR[0], t_PQR[2], stroke_width=8.0).set_color(YELLOW)

        self.play(
            Flash(A)
        )
        self.play(
            Flash(P)
        )

        self.play(
            ShowCreationThenDestruction(line_BC)
        )
        self.play(
            ShowCreationThenDestruction(line_QR)
        )
        self.play(
            Write(ratio[0])
        )

        self.play(
            Flash(B)
        )
        self.play(
            Flash(R)
        )
        
        self.play(
            ShowCreationThenDestruction(line_AC)
        )
        self.play(
            ShowCreationThenDestruction(line_PQ)
        )
        self.play(
            Write(ratio[1:3])
        )

        self.play(
            Flash(C)
        )
        self.play(
            Flash(Q)
        )
        self.play(
            ShowCreationThenDestruction(line_AB)
        )
        self.play(
            ShowCreationThenDestruction(line_PR)
        )
        self.play(
            Write(ratio[3:])
        )

        self.wait()

class JyeshtadevaLemma1(Scene):

    def construct(self):
        title = TextMobject("Observation - 1").scale(1.5)
        self.play(
            Write(title)
        )

        self.wait(0.5)
        self.play(
            ApplyMethod(title.to_edge, UP)
        )

        self.wait()

        lhs = TexMobject("\\frac{1}{1 + x}").set_color(RED).shift(UP)
        eq = TexMobject("=").shift(LEFT + UP)

        self.play(
            Write(lhs)
        )

        self.wait()
        self.play(
            ApplyMethod(lhs.next_to, eq, LEFT)
        )
        self.play(
            Write(eq)
        )

        rhs1 = TexMobject("\\frac{1 + x - x}{1 + x}").next_to(eq, RIGHT)
        self.wait(0.5)

        self.play(
            Write(rhs1)
        )
        self.wait()
        rhs2 = TexMobject("\\frac{1+x}{1+x}", "-", "\\frac{x}{1+x}").next_to(eq, RIGHT)
        self.play(
            ReplacementTransform(rhs1, rhs2)
        )
        self.wait(0.5)

        self.play(
            Transform(rhs2[0], TexMobject("1").next_to(eq, RIGHT))
        )

        self.play(
            ApplyMethod(
                rhs2[1:].next_to, rhs2[0], RIGHT
            )
        )

        temp = TexMobject("x", "\\left(", "\\frac{1}{1+x}", "\\right)")
        temp.next_to(rhs2[1], RIGHT)

        self.wait()
        self.play(
            Transform(rhs2[2], temp)
        )
        self.play(
            ApplyMethod(rhs2[1:].next_to, rhs2[0], RIGHT)
        )
        self.wait()
        temp[2].set_color(RED)
        temp.next_to(rhs2[1], RIGHT)
        self.play(
            Transform(rhs2[2], temp)
        )

        eq2 = TexMobject("=").next_to(eq, DOWN, buff=LARGE_BUFF*1.3)
        self.play(
            Write(eq2)
        )

        rhs3 = TexMobject("1", "-", "x", "\\left(", "1", "-", "x", "\\left(", "\\frac{1}{1+x}", "\\right)", "\\right)")
        rhs3.next_to(eq2)
        rhs3[8].set_color(RED)
        self.play(
            Write(rhs3[:4])
        )
        self.wait()
        self.play(
            TransformFromCopy(rhs2, rhs3[4:10])
        )
        self.play(
            Write(rhs3[-1])
        )

        eq3 = TexMobject("=").next_to(eq2, DOWN, buff=LARGE_BUFF*1.3)
        rhs4 = TexMobject("1 - x \\left(1 - x \\left(", "1 - x \\left(", "\\frac{1}{1+x}", "\\right)", "\\right)", "\\right)")
        rhs4[2].set_color(RED)
        rhs4.next_to(eq3, RIGHT)

        self.wait()
        self.play(
            Write(eq3),
            Write(rhs4[0])
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(rhs2, rhs4[1:4])
        )
        self.play(
            Write(rhs4[-2:])
        )

        vdots = TexMobject("\\vdots").next_to(eq3, DOWN, buff=MED_LARGE_BUFF).scale(1.5)
        self.play(
            Write(vdots)
        )
        
        get_rid = VGroup(lhs, eq, eq2, eq3, rhs2, rhs3, rhs4, vdots)

        self.play(
            Uncreate(get_rid)
        )

        self.wait()

        lemma = TexMobject("\\frac{1}{1+x}", "=", "1", "-", "x", "+", "x^2", "-", "x^3", "+", "\\cdots")

        self.play(
            Write(lemma[:2])
        )
        self.wait(0.5)

        self.play(
            Write(lemma[2])
        )
        self.wait(0.5)

        self.play(
            Write(lemma[3:5])
        )
        self.wait(0.5)

        self.play(
            Write(lemma[5:7])
        )
        self.wait(0.5)

        self.play(
            Write(lemma[7:9])
        )
        self.wait(0.5)

        self.play(
            Write(lemma[9:])
        )
        self.wait(0.5)

class Proof_Sum_of_n_Integers(Scene):
    CONFIG = {
        "l" : 0.5
    }

    def construct(self):

        boxes = VGroup()
        for i in range(6):
            for j in range(i + 1):
                b = Square(side_length=self.l, fill_opacity=0.6, color=GREEN)
                b.move_to(i * self.l * DOWN + j * self.l * RIGHT)
                boxes.add(b)

        
        t1 = TexMobject("1").add_updater(lambda m: m.next_to(boxes[0], LEFT))
        t2 = TexMobject("2").add_updater(lambda m: m.next_to(boxes[1], LEFT))
        t3 = TexMobject("3").add_updater(lambda m: m.next_to(boxes[3], LEFT))
        vdots = TexMobject("\\vdots").scale(1.4).add_updater(lambda m: m.next_to(t3, DOWN))
        tn = TexMobject("n").add_updater(lambda m: m.next_to(boxes[-6], LEFT))
        # self.add(t1, t2, t3, vdots, tn)
        # self.add(boxes.move_to(ORIGIN))

        lhs = TexMobject("S").scale(1.5)
        eq = TexMobject("=").scale(1.5)
        lhs.add_updater(lambda m: m.next_to(eq, LEFT))
        eq.shift(LEFT * 4)
        rhs = TexMobject("1 + 2 + 3 + 4 + \\cdots + n").scale(1.5).next_to(eq, RIGHT)

        self.play(
            Write(lhs),
            Write(eq),
            Write(rhs)
        )
        self.wait()

        rhs2 = TexMobject("\\sum_{r = 1}^{n} r").next_to(eq, RIGHT)
        self.play(
            Transform(rhs, rhs2)
        )

        self.wait(2)

        boxes.next_to(eq, RIGHT)
        boxes.shift(RIGHT)
        self.play(
            Uncreate(rhs)
        )
        self.play(
            ShowCreation(boxes[0])
        )
        self.wait(0.5)
        self.play(
            Write(t1)
        )
        self.wait()

        self.play(
            ShowCreation(boxes[1:3])
        )
        self.wait(0.5)
        self.play(
            Write(t2)
        )
        self.wait(0.5)
        self.play(
            ShowCreation(boxes[3:6])
        )
        self.wait(0.5)
        self.play(
            Write(t3)
        )
        self.wait(0.5)
        self.play(
            ShowCreation(boxes[6:])
        )
        self.wait(0.5)
        self.play(
            Write(tn),
            Write(vdots)
        )
        self.wait()

        l_brace = Brace(boxes, LEFT)
        l_len = TexMobject("n").next_to(l_brace, LEFT)

        get_rid = VGroup(t1, t2, t3, vdots, tn)

        self.play(
            ReplacementTransform(get_rid, l_brace),
            Write(l_len)
        )
        d_brace = Brace(boxes, DOWN)
        d_len = TexMobject("n").next_to(d_brace, DOWN)

        self.play(
            GrowFromCenter(d_brace),
            Write(d_len)
        )

        self.wait()

        plus = TexMobject(" + ").scale(1.5).next_to(boxes, RIGHT)
        boxes2 = boxes.copy()
        boxes2.next_to(plus, RIGHT)
        boxes2.shift(RIGHT)

        self.play(
            TransformFromCopy(boxes, boxes2)
        )

        self.play(
            Transform(lhs, TexMobject("2", "S").scale(1.5).next_to(eq, LEFT)),
            Write(plus)
        )

        self.wait()

        self.play(
            ApplyMethod(boxes2.rotate, PI, about_point=boxes2.get_left()[1] * UP + boxes2.get_bottom()[0] * RIGHT)
        )

        self.wait()

        self.play(
            Uncreate(plus)
        )

        self.play(
            ApplyMethod(
                boxes2.move_to, boxes.get_center() + self.l * RIGHT
            )
        )

        d_new_brace = Brace(VGroup(boxes, boxes2), DOWN)
        d_new_len = TexMobject("n + 1").next_to(d_new_brace, DOWN)

        self.wait()

        self.play(
            Transform(d_brace, d_new_brace),
            Transform(d_len, d_new_len)
        )

        self.wait()

        eq2 = TexMobject("=").scale(1.5).next_to(boxes2, RIGHT)
        eq2.shift(RIGHT)

        total = TexMobject("n", "(", "n + 1", ")").scale(1.5).next_to(eq2)

        self.play(
            Write(eq2),
            TransformFromCopy(l_len, total[0]),
            TransformFromCopy(d_len, total[2]),
            Write(total[1]),
            Write(total[-1])
        )

        get_rid = VGroup(boxes, boxes2, d_brace, l_brace, d_len, l_len, eq2)

        self.play(
            Uncreate(get_rid)
        )
        self.play(
            ApplyMethod(eq.move_to, ORIGIN)
        )
        self.play(
            ApplyMethod(total.next_to, eq, RIGHT)
        )

        self.wait()
        result = TexMobject("n(n+1)", "\\over", "2").scale(1.5).next_to(eq, RIGHT)
        lhs.clear_updaters()
        self.play(
            ApplyMethod(total.move_to, result[0]),
            ApplyMethod(lhs[0].move_to, result[-1])
        )
        self.play(
            Write(result[1])
        )

        the_sum = TexMobject("\\sum_{r=1}^{n}r").scale(1.5)
        eq2 = TexMobject("=").scale(1.5).next_to(lhs[1], LEFT)
        the_sum.next_to(eq2, LEFT)

        self.wait()
        self.play(
            Write(eq2),
            Write(the_sum)
        )

        self.wait()

class JyeshtadevaLemma2(Scene):
    
    def construct(self):
        title = TextMobject("Observation - 2").scale(1.5).to_edge(UP)
        self.play(
            FadeInFromDown(title)
        )
        self.wait()

        S = TexMobject("S")
        eq = TexMobject("=").shift(LEFT * 3)
        s1 = TexMobject("1 + 2 + 3 + \\cdots n")
        s1_not = TexMobject("\\sum_", "{r=1}", "^n", "r")
        
        S.next_to(eq, LEFT)
        s1.next_to(eq, RIGHT)
        s1_not.next_to(eq, RIGHT)

        self.play(
            Write(S),
            Write(eq)
        )
        self.play(
            Write(s1)
        )

        self.wait()
        self.play(
            Uncreate(s1)
        )

        self.play(
            Write(s1_not)
        )

        self.wait(3.5)
        eq2 = TexMobject("=").next_to(s1_not, RIGHT)
        rhs = TexMobject("n", "(", "n", "+", "1", ")", "\\over", "2").next_to(eq2, RIGHT)

        self.play(
            Write(eq2),
            Write(rhs)
        )

        arrow = Arrow(rhs.get_right(), rhs.get_right() + RIGHT*3)
        large_n = TextMobject("large n").next_to(arrow, DOWN)

        self.wait(2.0)
        self.play(
            GrowArrow(arrow)
        )
        self.play(
            Write(large_n)
        )
        rhs_large_n = TexMobject("n", "\\times n", "\\over", "2").next_to(arrow, RIGHT)
        self.wait(3.0)
        self.play(
            Write(rhs_large_n[2]),
            TransformFromCopy(rhs[-1], rhs_large_n[-1])
        )
        self.wait()
        self.play(
            TransformFromCopy(rhs[0], rhs_large_n[0])
        )
        self.play(
            TransformFromCopy(rhs[2], rhs_large_n[1])
        )
        self.wait()
        self.play(
            Transform(rhs_large_n, TexMobject("n^2", "\\over", "2").next_to(arrow, RIGHT))
        )

        self.wait()
        self.play(
            Uncreate(S),
            Uncreate(eq),
            Uncreate(s1_not),
            Uncreate(eq2),
            Uncreate(arrow),
            Uncreate(large_n),
            Uncreate(rhs_large_n),
            Uncreate(rhs),
        )


        eq = TexMobject("=").shift(LEFT * 3).scale(0.7)
        s2 = TexMobject("1^2 + 2^2 + 3^2 + \\cdots n^2").scale(0.7)
        s2_not = TexMobject("\\sum_", "{r=1}", "^n", "r^2").scale(0.7)
        
        s2.next_to(eq, LEFT)
        s2_not.next_to(eq, RIGHT)

        self.play(
            Write(s2),
            Write(eq)
        )
        self.play(
            Write(s2_not)
        )


        self.wait(3.0)
        eq2 = TexMobject("=").next_to(s2_not, RIGHT).scale(0.7)
        rhs = TexMobject("n", "(", "n", "+", "1", ")", "(", "2n", "+", "1", ")", "\\over", "6").scale(0.7).next_to(eq2, RIGHT)

        self.play(
            Write(eq2),
            Write(rhs)
        )

        arrow = Arrow(rhs.get_right(), rhs.get_right() + RIGHT*3).scale(0.7)
        large_n = TextMobject("large n").next_to(arrow, DOWN).scale(0.7)
        self.play(
            GrowArrow(arrow)
        )
        self.play(
            Write(large_n)
        )
        rhs_large_n = TexMobject("n", "\\times n", "\\times 2n", "\\over", "6").scale(0.7).next_to(arrow, RIGHT)
        self.wait()
        self.play(
            Write(rhs_large_n[3]),
            TransformFromCopy(rhs[-1], rhs_large_n[-1])
        )
        self.wait()
        self.play(
            TransformFromCopy(rhs[0], rhs_large_n[0])
        )
        self.play(
            TransformFromCopy(rhs[2], rhs_large_n[1])
        )
        self.play(
            TransformFromCopy(rhs[7], rhs_large_n[2])
        )
        self.wait()
        self.play(
            Transform(rhs_large_n, TexMobject("n^3", "\\over", "3").scale(0.7).next_to(arrow, RIGHT))
        )

        self.wait()
        self.play(
            Uncreate(s2),
            Uncreate(eq),
            Uncreate(s2_not),
            Uncreate(eq2),
            Uncreate(arrow),
            Uncreate(large_n),
            Uncreate(rhs_large_n),
            Uncreate(rhs),
        )

        self.wait()

        eq = TexMobject("=").shift(LEFT * 2)
        s2 = TexMobject("1^p + 2^p + 3^p + \\cdots n^p")
        s2_not = TexMobject("\\sum_", "{r=1}", "^n", "r^p")
        
        s2.next_to(eq, LEFT)
        s2_not.next_to(eq, RIGHT)

        self.play(
            Write(s2),
            Write(eq)
        )
        self.play(
            Write(s2_not)
        )

        arrow = Arrow(s2_not.get_right(), s2_not.get_right() + RIGHT*3)
        large_n = TextMobject("large n").next_to(arrow, DOWN)
        self.play(
            GrowArrow(arrow)
        )
        self.play(
            Write(large_n)
        )
        rhs_large_n = TexMobject("n^{p+1}", "\\over", "p+1").next_to(arrow, RIGHT)
        self.wait()
        self.play(
            Write(rhs_large_n)
        )
        
        self.wait()

class ProofOfMGL(ZoomedScene):

    CONFIG = {
        "r" : 6.0
    }

    def construct(self):
        box = Square(side_length=self.r)
        

        O = TexMobject("O").scale(0.7)
        O.add_updater(lambda m: m.next_to(box.get_corner(UL), UP))

        A = TexMobject("A").scale(0.7)
        A.add_updater(lambda m: m.next_to(box.get_corner(UR), UP))

        B = TexMobject("B").scale(0.7)
        B.add_updater(lambda m: m.next_to(box.get_corner(DR), DOWN))

        C = TexMobject("C").scale(0.7)
        C.add_updater(lambda m: m.next_to(box.get_corner(DL), DOWN))

        self.play(
            ShowCreation(box)
        )
        self.play(
            Write(A),
            Write(B),
            Write(C),
            Write(O)
        )

        self.wait(0.5)

        self.play(
            ApplyMethod(box.shift, LEFT * 3)
        )

        self.wait()

        line_OA = Line(box.get_corner(UL), box.get_corner(UR), stroke_width=8.0).set_color(YELLOW)
        # self.add(box, arc, O, A, B, C)

        self.play(
            ShowCreationThenDestruction(line_OA), run_time=1.5
        )

        self.wait(0.5)
        OA = TexMobject("O", "A").shift(RIGHT * 3 + UP * 2)

        eq = TexMobject("=").next_to(OA, RIGHT)
        one = TexMobject("1").next_to(eq, RIGHT)

        self.play(
            TransformFromCopy(O, OA[0]),
            TransformFromCopy(A, OA[1])
        )
        self.play(
            Write(eq),
            Write(one)
        )

        self.wait()
        
        self.wait()

        line_OA.add_tip()
        self.play(
            ShowCreation(line_OA)
        )

        def arc_tracer(m, alpha):
            m.restore()
            m.rotate(-PI/2 * alpha, about_point=box.get_corner(UL))

        line_OA.save_state()

        arc = ArcBetweenPoints(box.get_corner(UR), box.get_corner(DL), angle=-PI/2.0, stroke_width=4.0).set_color(DARK_BLUE)

        self.play(
            UpdateFromAlphaFunc(line_OA, arc_tracer),
            ShowCreation(arc)
        )

        self.wait()
        self.play(
            Uncreate(OA),
            Uncreate(eq),
            Uncreate(one),
            Uncreate(line_OA)
        )

        self.wait()

        #divide AB to n equal parts
        points = np.linspace(0.0, self.r, 8)
        Ps = VGroup(
            *[Dot().move_to(box.get_corner(UR) + DOWN * x).set_color(GOLD) for x in points]
        )

        self.play(
            AnimationGroup(
                *[GrowFromCenter(d) for d in Ps], lag_ratio=0.1, run_time=1.5
            )
        )
        eq_A = TexMobject("=").scale(0.7).next_to(A, RIGHT)
        P0 = TexMobject("P_0").scale(0.7).next_to(eq_A, RIGHT)

        eq_B = TexMobject("=").scale(0.7).next_to(B, RIGHT)
        Pn = TexMobject("P_n").scale(0.7).next_to(eq_B, RIGHT)

        self.play(
            Write(eq_A),
            Write(P0)
        )

        self.play(
            Write(eq_B),
            Write(Pn)
        )

        self.wait()

        self.play(
            FadeOut(Ps)
        )

        #example n = 2
        P2 = TexMobject("P_2").scale(0.7).next_to(eq_B, RIGHT)
        self.play(
            ReplacementTransform(Pn, P2)
        )
        eg_points = np.linspace(0.0, self.r, 3)
        eg_Ps = VGroup(
            *[Dot().move_to(box.get_corner(UR) + DOWN * x).set_color(GOLD) for x in eg_points]
        )

        self.play(
            AnimationGroup(
                *[GrowFromCenter(d) for d in eg_Ps], lag_ratio=0.1, run_time=1.5
            )
        )

        P1 = TexMobject("P_1").scale(0.7).next_to(eg_Ps[1])
        self.wait()
        self.play(
            Write(P1)
        )
        self.wait()
        self.play(
            FadeOut(A),
            FadeOut(eq_A),
            FadeOut(P0),
            FadeOut(P1)
        )
        eg_brace = Brace(VGroup(eg_Ps[0], eg_Ps[1]), RIGHT)
        delta = TexMobject("\\delta").next_to(eg_brace, RIGHT)
        eq_delta = TexMobject("=").next_to(delta, RIGHT)
        eg_delta_val = TexMobject("\\frac{1}{2}").next_to(eq_delta, RIGHT)

        self.play(
            GrowFromCenter(eg_brace)
        )
        self.play(
            Write(delta),
            Write(eq_delta),
            Write(eg_delta_val)
        )

        self.play(
            FadeOut(B),
            FadeOut(eq_B),
            FadeOut(P2)
        )

        self.play(
            ApplyMethod(eg_brace.shift, self.r/2.0 * DOWN),
            ApplyMethod(delta.shift, self.r/2.0 * DOWN),
            ApplyMethod(eq_delta.shift, self.r/2.0 * DOWN),
            ApplyMethod(eg_delta_val.shift, self.r/2.0 * DOWN)
        )

        self.wait(2.0)

        self.play(
            FadeOut(eg_brace),
            FadeOut(delta),
            FadeOut(eq_delta),
            FadeOut(eg_delta_val)
        )

        #example2 n = 3
        eg2_points = np.linspace(0.0, self.r, 4)
        eg2_Ps = VGroup(
            *[Dot().move_to(box.get_corner(UR) + DOWN * x).set_color(GOLD) for x in eg2_points]
        )

        self.play(
            ReplacementTransform(eg_Ps, eg2_Ps)
        )

        eg2_brace = Brace(VGroup(eg2_Ps[0], eg2_Ps[1]), RIGHT)
        delta = TexMobject("\\delta").next_to(eg2_brace, RIGHT)
        eq_delta = TexMobject("=").next_to(delta, RIGHT)
        eg2_delta_val = TexMobject("\\frac{1}{3}").next_to(eq_delta, RIGHT)

        self.play(
            GrowFromCenter(eg2_brace)
        )
        self.play(
            Write(delta),
            Write(eq_delta),
            Write(eg2_delta_val)
        )

        self.play(
            ApplyMethod(eg2_brace.shift, self.r/3.0 * DOWN),
            ApplyMethod(delta.shift, self.r/3.0 * DOWN),
            ApplyMethod(eq_delta.shift, self.r/3.0 * DOWN),
            ApplyMethod(eg2_delta_val.shift, self.r/3.0 * DOWN)
        )

        self.play(
            ApplyMethod(eg2_brace.shift, self.r/3.0 * DOWN),
            ApplyMethod(delta.shift, self.r/3.0 * DOWN),
            ApplyMethod(eq_delta.shift, self.r/3.0 * DOWN),
            ApplyMethod(eg2_delta_val.shift, self.r/3.0 * DOWN)
        )

        self.wait()

        self.play(
            FadeOut(eg2_brace),
            FadeOut(delta),
            FadeOut(eq_delta),
            FadeOut(eg2_delta_val)
        )

        self.wait()

        self.play(
            ReplacementTransform(eg2_Ps, Ps)
        )
        
        Pn = TexMobject("P_n").scale(0.7).next_to(eq_B, RIGHT)
        self.play(
            FadeIn(A),
            FadeIn(eq_A),
            FadeIn(P0),
            FadeIn(Pn),
            FadeIn(B),
            FadeIn(eq_B)
        )

        brace = Brace(VGroup(Ps[4], Ps[5]), RIGHT)
        delta.next_to(brace, RIGHT)
        eq_delta.next_to(delta, RIGHT)
        delta_val = TexMobject("1", "\\over", "n").next_to(eq_delta, RIGHT)

        self.wait()
        self.play(
            GrowFromCenter(brace)
        )
        self.play(
            Write(delta),
            Write(eq_delta),
            Write(delta_val)
        )

        self.wait()
        self.play(
            FadeOut(brace),
            ApplyMethod(delta.shift, RIGHT * 2),
            ApplyMethod(eq_delta.shift, RIGHT * 2),
            ApplyMethod(delta_val.shift, RIGHT * 2)
        )

        self.play(
            ApplyMethod(delta_val[2].move_to, delta.get_center() + LEFT * delta.get_width() * 1.5 + DOWN * delta.get_height() / 8.0),
            FadeOut(delta_val[1]),
            ApplyMethod(delta_val[0].next_to, eq_delta, RIGHT)
        )

        self.wait(2.0)

        self.play(
            FadeOut(delta),
            FadeOut(delta_val[0]),
            FadeOut(eq_delta),
            FadeOut(delta_val[2])
        )

        self.wait()

        Pr1 = TexMobject("P_{r-1}").scale(0.7).next_to(Ps[4], RIGHT)
        Pr = TexMobject("P_r").scale(0.7).next_to(Ps[5], RIGHT)

        self.play(
            Write(Pr1),
            Write(Pr)
        )
        self.wait()
        origin = Dot().move_to(box.get_corner(UL)).set_color(GOLD)
        self.play(
            GrowFromCenter(origin)
        )
        self.play(
            Flash(origin)
        )
        line_OPr1 = Line(origin, Ps[4], stroke_width=5.0).set_color(GREEN)
        line_OPr = Line(origin, Ps[5], stroke_width=5.0).set_color(GREEN)

        self.play(
            GrowArrow(line_OPr1)
        )
        self.play(
            GrowArrow(line_OPr)
        )
        #pts on the circle
        coord_E = origin.get_center() + self.r * np.array(
            [
                np.cos(np.arctan2(-points[4], self.r)),
                np.sin(np.arctan2(-points[4], self.r)),
                0.0
            ]
        )
        coord_G = origin.get_center() + self.r * np.array(
            [
                np.cos(np.arctan2(-points[5], self.r)),
                np.sin(np.arctan2(-points[5], self.r)),
                0.0
            ]
        )
        pt_E = Dot().move_to(coord_E).set_color(PURPLE)
        pt_G = Dot().move_to(coord_G).set_color(PURPLE)
        G = TexMobject("G").scale(0.7).set_color(PURPLE).next_to(pt_G, DOWN)
        E = TexMobject("E").scale(0.7).set_color(PURPLE).next_to(pt_E, UP)

        self.wait()
        self.play(
            GrowFromCenter(pt_E),
            Write(E)
        )
        self.play(
            GrowFromCenter(pt_G),
            Write(G)
        )

        self.wait()

        slope_EF = np.tan(PI/2.0 + np.arctan2(-points[5], self.r))
        slope_OPr = -points[5]/self.r
        x,y,z = origin.get_center()
        coord_F = origin.get_center() + np.array(
            [
                (-slope_EF * (coord_E[0]-x) + coord_E[1]-y)/(slope_OPr - slope_EF),
                (-slope_EF * (coord_E[0]-x) + coord_E[1]-y)/(slope_OPr - slope_EF) * slope_OPr,
                0.0
            ]
        ) 

        coord_D = origin.get_center() + np.array(
            [
                (-slope_EF * (Ps[4].get_center()[0]-x) + Ps[4].get_center()[1]-y)/(slope_OPr - slope_EF),
                (-slope_EF * (Ps[4].get_center()[0]-x) + Ps[4].get_center()[1]-y)/(slope_OPr - slope_EF) * slope_OPr,
                0.0
            ]
        ) 
        
        pt_F = Dot().move_to(coord_F).set_color(GOLD)
        pt_D = Dot().move_to(coord_D).set_color(GOLD)
        F = TexMobject("F").scale(0.7).next_to(pt_F, LEFT)
        D = TexMobject("D").scale(0.7).next_to(pt_D, DOWN)

        line_EF = Line(coord_F, coord_E).set_color(YELLOW)
        line_DPr1 = Line(coord_D, Ps[4]).set_color(YELLOW)

        self.play(
            GrowArrow(line_DPr1)
        )
        self.wait()
        self.play(
            GrowFromCenter(pt_D),
            Write(D)
        )

        self.wait()

        self.play(
            GrowArrow(line_EF)
        )
        self.wait()
        self.play(
            GrowFromCenter(pt_F),
            Write(F)
        )
        # angle_F_elb = Elbow(angle=np.arctan2(slope_EF, 1.0))
        # angle_F_elb.move_to(coord_F).shift((angle_F_elb.get_corner(UL) - angle_F_elb.get_center()) * angle_F_elb.get_width() / np.sqrt(2))
        # self.add(angle_F_elb)

        self.wait(2.0)

        self.camera_frame.save_state()
        focus_box = Rectangle().surround(VGroup(pt_E, pt_F))

        self.play(
            self.camera_frame.move_to, focus_box,
            self.camera_frame.set_width, focus_box.get_width()*2.0
        )

        self.wait(3.0)

        self.play(
            Restore(self.camera_frame)
        )

        self.wait(2.0)
        coord_O = origin.get_center()
        OEF = VGroup(
            Dot().move_to(coord_O),
            Dot().move_to(coord_E),
            Dot().move_to(coord_F),
            Line(coord_O, coord_E),
            Line(coord_E, coord_F),
            Line(coord_F, coord_O)
        ).set_color(RED)

        coord_Pr1 = Ps[4].get_center()
        ODPr1 = VGroup(
            Dot().move_to(coord_O),
            Dot().move_to(coord_D),
            Dot().move_to(coord_Pr1),
            Line(coord_O, coord_D),
            Line(coord_D, coord_Pr1),
            Line(coord_Pr1, coord_O)
        ).set_color(RED)

        def showcase_triangleOEF(m, alpha):
            m.restore()
            m.rotate(-np.arctan(slope_EF) * alpha, about_point=(coord_F + coord_E)/2.0)
            m.shift((RIGHT * 4 + DOWN*3.0) * alpha)

        def showcase_triangleODPr1(m, alpha):
            m.restore()
            m.rotate(-np.arctan(slope_EF) * alpha, about_point=(coord_D + coord_Pr1)/2.0)
            m.shift((RIGHT * 5 + DOWN*2.5) * alpha)

        OEF.save_state()
        self.play(
            ShowCreation(OEF)
        )
        self.play(
            UpdateFromAlphaFunc(OEF, showcase_triangleOEF)
        )
        OEF_O = TexMobject("O").scale(0.5).add_updater(lambda m:m.next_to(OEF[0], RIGHT, buff=0.2))
        OEF_E = TexMobject("E").scale(0.5).add_updater(lambda m:m.next_to(OEF[1], DOWN, buff=0.2))
        OEF_F = TexMobject("F").scale(0.5).add_updater(lambda m:m.next_to(OEF[2], DOWN, buff=0.2))

        self.play(
            Write(OEF_O),
            Write(OEF_E),
            Write(OEF_F),

        )

        ODPr1.save_state()
        self.play(
            ShowCreation(ODPr1)
        )
        self.play(
            UpdateFromAlphaFunc(ODPr1, showcase_triangleODPr1)
        )
        ODPr1_O = TexMobject("O").scale(0.5).add_updater(lambda m: m.next_to(ODPr1[0], RIGHT, buff=0.2))
        ODPr1_D = TexMobject("D").scale(0.5).add_updater(lambda m: m.next_to(ODPr1[1], DOWN, buff=0.2))
        ODPr1_Pr1 = TexMobject("P_{r-1}").scale(0.5).add_updater(lambda m: m.next_to(ODPr1[2], DR, buff=0.2))

        self.play(
            Write(ODPr1_O),
            Write(ODPr1_D),
            Write(ODPr1_Pr1),

        )

        self.wait()

        self.play(
            ApplyMethod(OEF.scale, 0.5),
            ApplyMethod(ODPr1.scale, 0.5)
        )

        self.play(
            ApplyMethod(OEF.shift, UP * 2),
            ApplyMethod(ODPr1.shift, UP * 1.5)
        )

        common_angle = TexMobject("\\angle O", "\\text{  is common}").shift(RIGHT * 4 + DOWN * 1).scale(0.7)
        ninenty_angle = TexMobject("\\angle F = \\angle D = 90^{\\circ}").next_to(common_angle, DOWN).scale(0.7)

        self.wait()
        self.play(
            Write(common_angle)
        )
        self.wait()
        self.play(
            Write(ninenty_angle)
        )

        self.wait()

        self.play(
            FadeOut(common_angle),
            FadeOut(ninenty_angle)
        )
        self.wait()
        similarity = TexMobject("\\bigtriangleup OEF", "\\sim" ,"\\bigtriangleup ODP_{r-1}").shift(RIGHT * 4 + DOWN * 1).scale(0.7)
        
        
        self.play(
            Write(similarity[0]),
            ShowCreationThenDestruction(OEF.copy().set_color(YELLOW))
        )
        self.wait(0.5)
        self.play(
            Write(similarity[2]),
            ShowCreationThenDestruction(ODPr1.copy().set_color(YELLOW))
        )
        self.play(
            Write(similarity[1]),
        )

        eq_EF = TextMobject("=").shift(RIGHT * 4 + DOWN * 2).scale(0.7)
        lhs_EF = TexMobject("EF", "\\over", "OE").scale(0.7).next_to(eq_EF, LEFT)
        rhs_EF = TexMobject("P_{r-1}D", "\\over", "OP_{r-1}").scale(0.7).next_to(eq_EF, RIGHT)

        self.wait()
        self.play(
            Write(lhs_EF[0]),
            Write(rhs_EF[0])
        )
        
        self.wait(2.0)
        self.play(
            Write(lhs_EF[1]),
            Write(rhs_EF[1]),
            Write(lhs_EF[2]),
            Write(rhs_EF[2])
        )
        self.wait(0.5)
        self.play(
            Write(eq_EF)
        )

        self.wait()

        self.play(
            Transform(lhs_EF[2], TexMobject("1").scale(0.7).move_to(lhs_EF[2]))
        )

        self.play(
            FadeOut(lhs_EF[1]),
            FadeOut(lhs_EF[2]),
            ApplyMethod(lhs_EF[0].next_to, eq_EF, LEFT)
        )

        self.wait()

        self.play(
            Uncreate(OEF),
            Uncreate(ODPr1),
            Uncreate(OEF_O),
            Uncreate(ODPr1_O),
            Uncreate(OEF_E),
            Uncreate(ODPr1_D),
            Uncreate(OEF_F),
            Uncreate(ODPr1_Pr1),
            Uncreate(similarity)

        )

        self.play(
            ApplyMethod(eq_EF.shift, UP*5),
            ApplyMethod(rhs_EF.shift, UP*5),
            ApplyMethod(lhs_EF[0].shift, UP*5),
        )

        self.wait()




        coord_Pr = Ps[5].get_center()
        Pr1PrD = VGroup(
            Dot().move_to(coord_Pr1),
            Dot().move_to(coord_Pr),
            Dot().move_to(coord_D),
            Line(coord_Pr, coord_Pr1),
            Line(coord_Pr1, coord_D),
            Line(coord_D, coord_Pr)
        ).set_color(RED)

        coord_A = box.get_corner(UR)
        OAPr = VGroup(
            Dot().move_to(coord_O),
            Dot().move_to(coord_A),
            Dot().move_to(coord_Pr),
            Line(coord_O, coord_A),
            Line(coord_A, coord_Pr),
            Line(coord_Pr, coord_O)
        ).set_color(RED)

        def showcase_trianglePr1PrD(m, alpha):
            m.restore()
            m.rotate(-np.arctan(slope_OPr) * alpha, about_point=(coord_D + coord_Pr)/2.0)
            
            m.shift((RIGHT * 6 + UP * 2) * alpha)

        def showcase_triangleOAPr(m, alpha):
            m.restore()
            m.rotate(-PI/2 * alpha, about_point=(coord_A + coord_Pr)/2.0)
            m.shift((RIGHT * 2.5 + DOWN*2.5) * alpha)

        Pr1PrD.save_state()
        self.play(
            ShowCreation(Pr1PrD)
        )
        self.play(
            UpdateFromAlphaFunc(Pr1PrD, showcase_trianglePr1PrD)
        )
        Pr1PrD_O = TexMobject("P_{r-1}").scale(0.5).add_updater(lambda m:m.next_to(Pr1PrD[0], RIGHT, buff=0.2))
        Pr1PrD_E = TexMobject("P_r").scale(0.5).add_updater(lambda m:m.next_to(Pr1PrD[1], DOWN, buff=0.2))
        Pr1PrD_F = TexMobject("D").scale(0.5).add_updater(lambda m:m.next_to(Pr1PrD[2], DOWN, buff=0.2))

        self.play(
            Write(Pr1PrD_O),
            Write(Pr1PrD_E),
            Write(Pr1PrD_F),

        )

        OAPr.save_state()
        self.play(
            ShowCreation(OAPr)
        )
        self.play(
            UpdateFromAlphaFunc(OAPr, showcase_triangleOAPr)
        )
        self.play(
            ApplyMethod(OAPr.scale, 0.4)
        )
        OAPr_O = TexMobject("O").scale(0.5).add_updater(lambda m: m.next_to(OAPr[0], RIGHT, buff=0.2))
        OAPr_D = TexMobject("A").scale(0.5).add_updater(lambda m: m.next_to(OAPr[1], DOWN, buff=0.2))
        OAPr_Pr1 = TexMobject("P_{r}").scale(0.5).add_updater(lambda m: m.next_to(OAPr[2], DOWN, buff=0.2))

        self.play(
            Write(OAPr_O),
            Write(OAPr_D),
            Write(OAPr_Pr1),

        )

        self.wait()

        # self.play(
        #     ApplyMethod(OAPr.scale, 0.4/0.6),
        # )

        

        self.wait()

        common_angle = TexMobject("\\angle P_{r}", "\\text{  is common}").shift(RIGHT * 4 + DOWN * 1).scale(0.7)
        ninenty_angle = TexMobject("\\angle A = \\angle D = 90^{\\circ}").next_to(common_angle, DOWN).scale(0.7)

        self.play(
            Write(common_angle)
        )
        self.wait()
        self.play(
            Write(ninenty_angle)
        )
        self.wait()

        self.play(
            FadeOut(common_angle),
            FadeOut(ninenty_angle)
        )

        similarity = TexMobject("\\bigtriangleup P_{r-1}P_{r}D", "\\sim" ,"\\bigtriangleup OAP_{r}").shift(RIGHT * 4 + DOWN * 1).scale(0.7)
        self.wait()
        self.play(
            Write(similarity[0]),
            ShowCreationThenDestruction(Pr1PrD.copy().set_color(YELLOW))
        )
        self.wait(0.5)
        self.play(
            Write(similarity[2]),
            ShowCreationThenDestruction(OAPr.copy().set_color(YELLOW))
        )
        self.play(
            Write(similarity[1]),
        )

        eq_Pr1D = TextMobject("=").shift(RIGHT * 4 + DOWN * 2).scale(0.7)
        lhs_Pr1D = TexMobject("P_{r-1}D", "\\over", "OA").scale(0.7).next_to(eq_Pr1D, LEFT)
        rhs_Pr1D = TexMobject("P_{r-1}P_r", "\\over", "OP_{r}").scale(0.7).next_to(eq_Pr1D, RIGHT)

        self.wait()
        self.play(
            Write(lhs_Pr1D[0]),
            Write(rhs_Pr1D[0])
        )

        self.wait()
        self.play(
            Write(lhs_Pr1D[1]),
            Write(rhs_Pr1D[1]),
            Write(lhs_Pr1D[2]),
            Write(rhs_Pr1D[2])
        )
        self.wait(0.5)
        self.play(
            Write(eq_Pr1D)
        )

        self.wait()

        self.play(
            Transform(lhs_Pr1D[2], TexMobject("1").scale(0.7).move_to(lhs_Pr1D[2]))
        )

        self.play(
            FadeOut(lhs_Pr1D[1]),
            FadeOut(lhs_Pr1D[2]),
            ApplyMethod(lhs_Pr1D[0].next_to, eq_Pr1D, LEFT)
        )

        self.wait()

        self.play(
            Uncreate(Pr1PrD),
            Uncreate(OAPr),
            Uncreate(Pr1PrD_O),
            Uncreate(OAPr_O),
            Uncreate(Pr1PrD_E),
            Uncreate(OAPr_D),
            Uncreate(Pr1PrD_F),
            Uncreate(OAPr_Pr1),
            Uncreate(similarity)

        )

        self.play(
            ApplyMethod(eq_Pr1D.shift, UP*4),
            ApplyMethod(rhs_Pr1D.shift, UP*4),
            ApplyMethod(lhs_Pr1D[0].shift, UP*4),
        )

        self.wait()

        implies = TexMobject("\\Downarrow").next_to(eq_Pr1D, DOWN)

        self.play(
            FadeInFrom(implies, UP)
        )

        val_EF = TexMobject("EF", "=", "\\frac{P_{r-1} P_r}{OP_{r-1} \\cdot OP_r}").scale(0.7).next_to(implies, DOWN)

        self.play(
            Write(val_EF)
        )

        arc_EG = TexMobject("\\text{arc }", "EG").scale(0.7).set_color(DARK_BLUE)
        nearly_eq = TexMobject("\\approx").scale(0.7).next_to(val_EF, LEFT)
        arc_EG.next_to(nearly_eq, LEFT)

        self.wait()
        self.play(
            Write(nearly_eq),
            Write(arc_EG)
        )

        self.wait()
        self.play(
            Uncreate(eq_EF),
            Uncreate(lhs_EF[0]),
            Uncreate(rhs_EF),
            Uncreate(eq_Pr1D),
            Uncreate(lhs_Pr1D[0]),
            Uncreate(rhs_Pr1D),
            FadeOut(implies),
            Uncreate(val_EF[0]),
            Uncreate(val_EF[1]),
            ApplyMethod(nearly_eq.next_to, val_EF[2], LEFT)
        )
        self.play(
            ApplyMethod(arc_EG.next_to, nearly_eq, LEFT)
        )

        self.wait()
        self.play(
            FadeOut(E),
            FadeOut(G),
            FadeOut(F),
            FadeOut(D),
            FadeOut(Pr),
            FadeOut(Pr1),
            FadeOut(pt_E),
            FadeOut(pt_G),
            FadeOut(pt_F),
            FadeOut(pt_D),
            FadeOut(line_DPr1),
            FadeOut(line_EF),
            FadeOut(line_OPr),
            FadeOut(line_OPr1)
        )

        self.wait()
        largeN1_points = np.linspace(0.0, self.r, 30)
        largeN1_Ps = VGroup(
            *[Dot(radius=0.05).move_to(box.get_corner(UR) + DOWN * x).set_color(GOLD) for x in largeN1_points]
        )

        self.play(
            ReplacementTransform(Ps, largeN1_Ps)
        )

        largeN2_points = np.linspace(0.0, self.r, 50)
        largeN2_Ps = VGroup(
            *[Dot(radius=0.05).move_to(box.get_corner(UR) + DOWN * x).set_color(GOLD) for x in largeN2_points]
        )

        self.wait()
        self.play(
            ReplacementTransform(largeN1_Ps, largeN2_Ps)
        )

        line_OPr1 = Line(origin, largeN2_Ps[35], stroke_width=0.8).set_color(GREEN)
        line_OPr = Line(origin, largeN2_Ps[36], stroke_width=0.8).set_color(GREEN)

        self.play(
            GrowArrow(line_OPr1)
        )
        self.play(
            GrowArrow(line_OPr)
        )
        #pts on the circle
        coord_E = origin.get_center() + self.r * np.array(
            [
                np.cos(np.arctan2(-largeN2_points[35], self.r)),
                np.sin(np.arctan2(-largeN2_points[35], self.r)),
                0.0
            ]
        )
        coord_G = origin.get_center() + self.r * np.array(
            [
                np.cos(np.arctan2(-largeN2_points[36], self.r)),
                np.sin(np.arctan2(-largeN2_points[36], self.r)),
                0.0
            ]
        )

        slope_EF = np.tan(PI/2.0 + np.arctan2(-largeN2_points[36], self.r))
        slope_OPr = -largeN2_points[36]/self.r
        x,y,z = origin.get_center()
        coord_F = origin.get_center() + np.array(
            [
                (-slope_EF * (coord_E[0]-x) + coord_E[1]-y)/(slope_OPr - slope_EF),
                (-slope_EF * (coord_E[0]-x) + coord_E[1]-y)/(slope_OPr - slope_EF) * slope_OPr,
                0.0
            ]
        ) 

        
        line_EF = Line(coord_F, coord_E).set_color(YELLOW)

        

        self.wait()

        self.play(
            GrowArrow(line_EF)
        )
        self.wait()
        
        # angle_F_elb = Elbow(angle=np.arctan2(slope_EF, 1.0))
        # angle_F_elb.move_to(coord_F).shift((angle_F_elb.get_corner(UL) - angle_F_elb.get_center()) * angle_F_elb.get_width() / np.sqrt(2))
        # self.add(angle_F_elb)

        self.wait(2.0)
        pt_E = Dot().move_to(coord_E)
        pt_F = Dot().move_to(coord_F)
        self.camera_frame.save_state()
        focus_box = Rectangle().surround(VGroup(pt_E, pt_F))

        self.play(
            self.camera_frame.move_to, focus_box,
            self.camera_frame.set_width, focus_box.get_width()*2.5
        )

        self.wait(3.0)

        self.play(
            Restore(self.camera_frame)
        )

        self.wait()
        num_val = TexMobject("P_{r-1}P_r", "=", "\\delta").scale(0.7).next_to(nearly_eq, DOWN, buff=0.8)
        den_equivalence = TexMobject("OP_{r-1}", "\\approx", "OP_r").scale(0.7).next_to(num_val, DOWN)
        
        self.play(
            Write(num_val)
        )
        self.wait()
        self.play(
            Write(den_equivalence)
        )

        rhs_EG = TexMobject("P_{r-1}P_r", "\\over", "OP_{r-1} \\cdot OP_{r}").scale(0.7).move_to(val_EF[2])
        self.add(rhs_EG)
        self.remove(val_EF[2])

        self.wait()
        self.play(
            Transform(rhs_EG[0], TexMobject("\\delta").scale(0.7).move_to(rhs_EG[0]))
        )

        self.play(
            Transform(rhs_EG[2], TexMobject("OP_r^2").scale(0.7).move_to(rhs_EG[2]))
        )

        self.play(
            Uncreate(num_val),
            Uncreate(den_equivalence)
        )

        self.wait()

        self.play(
            ShowCreationThenDestruction(Line(coord_O, coord_Pr, stroke_width=8.0).set_color(YELLOW))
        )
        self.wait()
        self.play(
            ShowCreationThenDestruction(Line(coord_O, coord_A, stroke_width=8.0).set_color(YELLOW)),
            ShowCreationThenDestruction(Line(coord_Pr, coord_A, stroke_width=8.0).set_color(YELLOW))
        )

        self.wait()
        self.play(
            Transform(rhs_EG[2], TexMobject("OA^2 + AP_r^2").scale(0.7).move_to(rhs_EG[2]))
        )
        self.wait()

        self.play(
            Transform(rhs_EG[2], TexMobject("1 + AP_r^2").scale(0.7).move_to(rhs_EG[2]))
        )

        self.wait()

        self.play(
            Transform(rhs_EG[2], TexMobject("1 + r^2\\delta^2").scale(0.7).move_to(rhs_EG[2]))
        )

        self.wait()
        self.remove(line_OPr, line_OPr1, line_EF)

        lines = []
        for i in range(len(largeN2_points)-1):
            line_OPr1 = Line(origin, largeN2_Ps[i], stroke_width=0.8).set_color(GREEN)
            line_OPr = Line(origin, largeN2_Ps[i+1], stroke_width=0.8).set_color(GREEN)

        
            #pts on the circle
            coord_E = origin.get_center() + self.r * np.array(
                [
                    np.cos(np.arctan2(-largeN2_points[i], self.r)),
                    np.sin(np.arctan2(-largeN2_points[i], self.r)),
                    0.0
                ]
            )

            slope_EF = np.tan(PI/2.0 + np.arctan2(-largeN2_points[36], self.r))
            slope_OPr = -largeN2_points[i+1]/self.r
            x,y,z = origin.get_center()
            coord_F = origin.get_center() + np.array(
                [
                    (-slope_EF * (coord_E[0]-x) + coord_E[1]-y)/(slope_OPr - slope_EF),
                    (-slope_EF * (coord_E[0]-x) + coord_E[1]-y)/(slope_OPr - slope_EF) * slope_OPr,
                    0.0
                ]
            ) 

            
            line_EF = Line(coord_F, coord_E).set_color(YELLOW)

            if i == 0:
                a = line_OPr
                b = line_OPr1
                c = line_EF
                lines.append(a)
                lines.append(b)
                # lines.append(c)
                self.play(
                    ShowCreation(a),
                    ShowCreation(b),
                    ShowCreation(c),
                    run_time=1.5/len(largeN2_points)
                )

            else:
                lines.append(line_OPr)
                lines.append(line_OPr1)
                # lines.append(line_EF)
                self.play(
                    Transform(a, line_OPr),
                    Transform(b, line_OPr1),
                    Transform(c, line_EF),
                    run_time=1.5/len(largeN2_points)
                )
                # if i == len(largeN2_points)-1:
                #     self.play(
                #         FadeOut(a),
                #         FadeOut(b),
                #         FadeOut(c)
                #     )



        self.play(
            Uncreate(rhs_EG),
            Uncreate(nearly_eq),
            Uncreate(arc_EG)
        )
        self.wait()
        lines.reverse()
        self.play(
            AnimationGroup(
                *[ShowCreation(l) for l in lines],lag_ratio=0.2, run_time=1.5
            ),
            ShowCreation(ArcBetweenPoints(origin.get_center() + self.r * np.array([np.cos(PI/4), -np.sin(PI/4), 0.0]), coord_A, angle=PI/4.0).set_color(YELLOW), run_time=2.0)
        )
        self.wait()

        equal1 = TexMobject("=").scale(0.7).shift(RIGHT * 1.5 + UP*2)
        large_n = TexMobject("\\text{large }", "n", "\\Bigg[").scale(0.7).next_to(equal1, RIGHT)
        sum_symbol = TexMobject("\\sum_", "{r=1}", "^n").scale(0.7).next_to(large_n, RIGHT, buff=0.1)
        rhs = TexMobject("\\delta", "\\over", "1 + r^2\\delta^2").scale(0.7).next_to(sum_symbol, RIGHT)
        close_bracket = TexMobject("\\Bigg]").scale(0.7).next_to(rhs, RIGHT)
        half_AC = TexMobject("AC", "\\over", "2").scale(0.7).next_to(equal1, LEFT)
        
        self.play(
            Write(rhs)
        )
        self.play(
            Write(sum_symbol)
        )
        self.play(
            Write(large_n),
            Write(close_bracket)
        )
        self.play(
            Write(half_AC),
            Write(equal1)
        )

        self.wait(2.0)

        self.play(
            Transform(half_AC[0], TexMobject("2\\pi/4").scale(0.7).move_to(half_AC[0]))
        )
        self.wait()

        self.play(
            Transform(half_AC, TexMobject("\\pi", "\\over", "4").scale(0.7).move_to(half_AC))
        )

        self.wait()

        equal2 = TexMobject("=").scale(0.7).next_to(equal1, DOWN, buff=1.3)
        large_n2 = TexMobject("\\text{large }", "n", "\\Bigg[").scale(0.7).next_to(equal2, RIGHT, buff=0.1)
        delta = TexMobject("\\delta").scale(0.7).next_to(large_n2, RIGHT, buff=0.1)
        sum_symbol2 = TexMobject("\\sum_", "{r=1}", "^n").scale(0.7).next_to(delta, RIGHT, buff=0.1)
        rhs2 = TexMobject("\\left(", "1", "\\over", "1 + r^2\\delta^2", "\\right)").scale(0.7).next_to(sum_symbol2, RIGHT)
        close_bracket2 = TexMobject("\\Bigg]").scale(0.7).next_to(rhs2, RIGHT)

        self.play(
            Write(equal2),
            Write(large_n2),
            Write(sum_symbol2),
            Write(rhs2),
            Write(delta),
            Write(close_bracket2)
        )

        self.wait()
        rhs3 = TexMobject("\\left(", "1", "-", "\\delta^2 r^2", "+", "\\delta^4 r^4", "-", "\\cdots", "\\right)").scale(0.5).next_to(sum_symbol2, RIGHT, buff=0.1)
        self.play(
            FadeOut(close_bracket2),
            Transform(rhs2, rhs3)
        )
        close_bracket2.next_to(rhs3, RIGHT, buff=0.1)
        self.play(
            FadeIn(close_bracket2)
        )

        self.wait()

        equal3 = TexMobject("=").scale(0.6).next_to(equal2, DOWN, buff=1.3)
        large_n3 = TexMobject("\\text{large }", "n", "\\Bigg[").scale(0.4).next_to(equal3, RIGHT, buff=0.1)
        delta_1 = TexMobject("\\delta").scale(0.6).next_to(large_n3, RIGHT, buff=0.05)
        s1 = TexMobject("\\sum_{r=1}^n", "1").scale(0.6).next_to(delta_1, RIGHT, buff=0.1)
        m1 = TexMobject("-").scale(0.6).next_to(s1, RIGHT, buff=0.1)
        delta_3 = TexMobject("\\delta^3").scale(0.6).next_to(m1, RIGHT, buff=0.1)
        s3 = TexMobject("\\sum_{r=1}^n", "r^2").scale(0.6).next_to(delta_3, RIGHT, buff=0.1)
        m3 = TexMobject("+").scale(0.6).next_to(s3, RIGHT, buff=0.1)
        delta_5 = TexMobject("\\delta^5").scale(0.6).next_to(m3, RIGHT, buff=0.1)
        s5 = TexMobject("\\sum_{r=1}^n", "r^4").scale(0.6).next_to(delta_5, RIGHT, buff=0.1)
        m5 = TexMobject("-").scale(0.6).next_to(s5, RIGHT, buff=0.1)
        cdots = TexMobject("\\cdots").scale(0.6).next_to(m5, RIGHT, buff=0.1)
        close_bracket3 = TexMobject("\\Bigg]").scale(0.6).next_to(cdots, RIGHT, buff=0.1)

        self.play(
            Write(equal3), 
            Write(large_n3), 
            Write(s1),  
            Write(delta_1), 
        )
        self.play(
            Write(m1),
            Write(s3),  
            Write(delta_3), 
        )
        self.play(
            Write(m3),
            Write(s5),  
            Write(delta_5), 
        )
        self.play(
            Write(m5),
            Write(cdots), 
            Write(close_bracket3)
            )

        self.wait()
        self.play(
            Transform(s1, TexMobject("n").scale(0.6).move_to(delta_1.get_center() + RIGHT * delta_1.get_width() * 1.5 + DOWN * delta_1.get_height() / 8.0))
        )
        self.wait()
        self.play(
            Transform(s3, TexMobject("n^3", "\\over", "3").scale(0.6).move_to(delta_3.get_center() + RIGHT * delta_3.get_width() * 1.5))
        )
        self.wait()
        self.play(
            Transform(s5, TexMobject("n^5", "\\over", "5").scale(0.6).move_to(delta_5.get_center() + RIGHT * delta_5.get_width() * 1.5 ))
        )

        self.wait()
        self.play(
            Uncreate(close_bracket3),
            Uncreate(s1),  
            Uncreate(delta_1), 
            Uncreate(m1),
            Uncreate(s3),  
            Uncreate(delta_3), 
            Uncreate(m3),
            Uncreate(s5),  
            Uncreate(delta_5), 
            Uncreate(m5),
            Uncreate(cdots)
        )
        t1 = TexMobject("\\delta n").scale(0.6).next_to(large_n3, RIGHT, buff=0.1)
        m1 = TexMobject("-").scale(0.6).next_to(t1, RIGHT, buff=0.1)
        t2 = TexMobject("(\\delta n)^3", "\\over", "3").scale(0.6).next_to(m1, RIGHT, buff=0.1).shift(UP * 0.05)
        m2 = TexMobject("+").scale(0.6).next_to(t2, RIGHT, buff=0.1).shift(DOWN * 0.05)
        t3 = TexMobject("(\\delta n)^5", "\\over", "5").scale(0.6).next_to(m2, RIGHT, buff=0.1).shift(UP * 0.05)
        m3 = TexMobject("-").scale(0.6).next_to(t3, RIGHT, buff=0.1).shift(DOWN * 0.05)
        cdots = TexMobject("\\cdots").scale(0.6).next_to(m3, RIGHT, buff=0.1)
        close_bracket3 = TexMobject("\\Bigg]").scale(0.6).next_to(cdots, RIGHT, buff=0.1)

        self.play(
            Write(t1),
            Write(m1),
            Write(t2),
            Write(m2),
            Write(t3),
            Write(m3),
            Write(cdots),
            Write(close_bracket3),
        )

        self.wait()

        self.play(
            Transform(t1, TexMobject("1").scale(0.6).move_to(t1))
        )
        self.play(
            Transform(t2[0], TexMobject("1").scale(0.6).move_to(t2[0]))
        )
        self.play(
            Transform(t3[0], TexMobject("1").scale(0.6).move_to(t3[0]))
        )

        self.wait()

        self.play(
            Uncreate(large_n3),
            Uncreate(close_bracket3)
        )

        self.wait()
        self.clear()

        series = TexMobject("\\frac{\\pi}{4}", "= ", "1 ", "- ", "\\frac{1}{3}", "+ ", "\\frac{1}{5}", "- ", "\\frac{1}{7}", "+ ", "\\frac{1}{9}", "-",  "\\cdots")

        series.scale(2).set_color("#90be6d")

        self.play(
            Write(
                series[:2]
            )
        )
        self.wait()
        self.play(
            Write(
                series[2]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[3:5]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[5:7]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[7:9]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[9:11]
            )
        )
        self.wait(0.5)
        self.play(
            Write(
                series[11:]
            )
        )
        self.wait(0.5)

        self.wait()

SCENES_IN_ORDER = [
    WhatIsPI,
    ValueOfPI,
    SeriesIntro,
    SimilarTriangles,
    JyeshtadevaLemma1,
    JyeshtadevaLemma2,
    ProofOfMGL,
    Proof_Sum_of_n_Integers
]


