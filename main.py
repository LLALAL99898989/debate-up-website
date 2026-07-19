from flask import Flask

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Debate Up | Empowering Grades 6–8</title>

    <meta name="description"
          content="Debate Up empowers students in grades 6–8 to build confidence, communication, critical thinking, and leadership through debate.">

    <style>

        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700;800&display=swap');

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            font-family: 'Inter', sans-serif;
            color: #10243a;
            background: white;
            line-height: 1.65;
        }


        /* NAVIGATION */

        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(255, 255, 255, 0.97);
            border-bottom: 1px solid #eeeeee;
        }

        nav {
            max-width: 1150px;
            margin: auto;
            padding: 18px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 30px;
        }

        .brand {
            font-size: 21px;
            font-weight: 800;
            letter-spacing: 2px;
            color: #062d57;
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            gap: 24px;
            align-items: center;
        }

        .nav-links a {
            text-decoration: none;
            color: #10243a;
            font-weight: 600;
            font-size: 14px;
            transition: 0.2s;
        }

        .nav-links a:hover {
            color: #8b1835;
        }

        .nav-button {
            background: #8b1835;
            color: white !important;
            padding: 10px 18px;
            border-radius: 6px;
        }


        /* GENERAL */

        .container {
            width: 90%;
            max-width: 1120px;
            margin: auto;
        }

        section {
            padding: 90px 0;
        }

        .eyebrow {
            color: #8b1835;
            font-weight: 800;
            letter-spacing: 3px;
            font-size: 12px;
        }

        h1 {
            font-family: 'DM Serif Display', serif;
            font-size: clamp(50px, 7vw, 90px);
            font-weight: 400;
            line-height: 1;
            color: #062d57;
            margin: 20px 0;
        }

        h1 span {
            color: #8b1835;
        }

        h2 {
            font-family: 'DM Serif Display', serif;
            font-size: clamp(35px, 5vw, 55px);
            font-weight: 400;
            line-height: 1.1;
            color: #062d57;
            margin: 10px 0 25px;
        }

        h3 {
            color: #062d57;
            font-size: 21px;
            font-weight: 700;
        }

        p {
            font-size: 16px;
        }


        /* BUTTONS */

        .button {
            display: inline-block;
            background: #8b1835;
            color: white;
            padding: 14px 25px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 700;
            border-radius: 6px;
            margin-right: 10px;
            margin-top: 15px;
            transition: 0.2s;
        }

        .button:hover {
            transform: translateY(-3px);
        }

        .button-outline {
            background: transparent;
            color: #062d57;
            border: 2px solid #062d57;
        }


        /* HERO */

        .hero {
            min-height: 85vh;
            display: flex;
            align-items: center;

            background: linear-gradient(
                120deg,
                #fff7e8,
                #ffffff
            );
        }

        .hero-content {
            max-width: 850px;
        }

        .hero-text {
            font-size: 19px;
            max-width: 700px;
            color: #46586a;
            line-height: 1.7;
        }


        /* MISSION */

        .mission {
            max-width: 850px;
        }


        /* PROGRAM */

        .cream {
            background: #fff7e8;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
            margin-top: 45px;
        }

        .card {
            background: white;
            padding: 35px;
            border-radius: 14px;
            border-top: 5px solid #8b1835;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.07);
            transition: 0.25s;
        }

        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 16px 35px rgba(0, 0, 0, 0.10);
        }

        .number {
            color: #e8b04a;
            font-size: 17px;
            font-weight: 800;
        }


        /* IMPACT */

        .impact {
            background: #062d57;
            color: white;
        }

        .impact h2 {
            color: white;
        }

        .impact-container {
            display: grid;
            grid-template-columns: 1fr 1.5fr;
            align-items: center;
            gap: 70px;
        }

        .big-number {
            font-family: 'DM Serif Display', serif;
            font-size: 135px;
            line-height: 1;
        }

        .big-number span {
            color: #e8b04a;
        }

        .stat-label {
            font-size: 13px;
            letter-spacing: 3px;
            font-weight: 800;
        }

        .light {
            color: #e8b04a;
        }


        /* SKILLS */

        .skill-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 45px;
        }

        .skill {
            padding: 30px;
            border-radius: 12px;
            background: #fff7e8;
            border-bottom: 4px solid #8b1835;
            transition: 0.2s;
        }

        .skill:hover {
            transform: translateY(-4px);
        }


        /* GET INVOLVED */

        .application-link {
            color: #8b1835;
            text-decoration: none;
            font-size: 14px;
            font-weight: 800;
        }

        .application-link:hover {
            text-decoration: underline;
        }


        /* CONTACT */

        .contact {
            background: #8b1835;
            color: white;
        }

        .contact h2 {
            color: white;
        }

        .contact-content {
            max-width: 750px;
        }

        .email-button {
            display: inline-block;
            background: #e8b04a;
            color: #062d57;
            padding: 15px 25px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 700;
            text-decoration: none;
            margin-top: 15px;
        }


        /* FOOTER */

        footer {
            background: #041f3c;
            color: #c9d2dc;
            padding: 45px 5%;
            text-align: center;
        }

        footer h3 {
            color: white;
            letter-spacing: 2px;
            font-weight: 800;
        }

        footer p {
            font-size: 13px;
        }


        /* MOBILE */

        @media (max-width: 850px) {

            .nav-links {
                display: none;
            }

            .cards {
                grid-template-columns: 1fr;
            }

            .skill-grid {
                grid-template-columns: 1fr;
            }

            .impact-container {
                grid-template-columns: 1fr;
            }

            .big-number {
                font-size: 90px;
            }

            section {
                padding: 65px 0;
            }

            .hero {
                min-height: auto;
                padding: 90px 0;
            }

        }

    </style>

</head>


<body>


<!-- NAVIGATION -->

<header>

    <nav>

        <a href="#home" class="brand">
            DEBATE UP
        </a>

        <div class="nav-links">

            <a href="#about">
                About
            </a>

            <a href="#program">
                Our Program
            </a>

            <a href="#impact">
                Impact
            </a>

            <a href="#skills">
                Student Growth
            </a>

            <a href="#get-involved">
                Get Involved
            </a>

            <a href="#contact">
                Contact
            </a>

            <a href="#get-involved"
               class="nav-button">
                JOIN US
            </a>

        </div>

    </nav>

</header>



<!-- HERO -->

<section class="hero" id="home">

    <div class="container">

        <div class="hero-content">

            <div class="eyebrow">
                EMPOWERING STUDENTS IN GRADES 6–8
            </div>

            <h1>
                Building Confidence.
                <br>
                <span>
                    Finding Voices.
                </span>
            </h1>

            <p class="hero-text">

                Debate Up empowers students in grades 6–8
                to become confident speakers, critical thinkers,
                and strong communicators through interactive
                debate sessions and competitions.

            </p>

            <a href="#get-involved"
               class="button">

                JOIN OUR PROGRAM

            </a>

            <a href="#about"
               class="button button-outline">

                LEARN MORE

            </a>

        </div>

    </div>

</section>



<!-- ABOUT -->

<section id="about">

    <div class="container mission">

        <div class="eyebrow">
            OUR MISSION
        </div>

        <h2>
            Every student deserves to know that their voice matters.
        </h2>

        <p>

            Debate Up is a 501(c)(3) nonprofit organization
            dedicated to empowering students in grades 6–8.

            We help students strengthen their confidence,
            public speaking, communication, and critical-thinking
            skills in an encouraging and supportive environment.

        </p>

        <p>

            Through interactive lessons, hands-on practice,
            and debate competitions, students learn to express
            their ideas, step outside their comfort zones,
            and become more confident in themselves both inside
            and outside the classroom.

        </p>

        <p>

            Our goal goes beyond teaching students how to debate.
            We want every student who participates in Debate Up
            to recognize that their ideas matter and feel
            confident using their voice.

        </p>

    </div>

</section>



<!-- OUR PROGRAM -->

<section class="cream" id="program">

    <div class="container">

        <div class="eyebrow">
            OUR PROGRAM
        </div>

        <h2>
            Confidence built through experience.
        </h2>

        <p>

            Our sessions give students the opportunity to
            learn new skills, practice in a supportive
            environment, and put their abilities into action.

        </p>


        <div class="cards">


            <div class="card">

                <div class="number">
                    01
                </div>

                <h3>
                    Learn
                </h3>

                <p>

                    Students build skills in public speaking,
                    argument development, communication,
                    critical thinking, and effective
                    presentation.

                </p>

            </div>


            <div class="card">

                <div class="number">
                    02
                </div>

                <h3>
                    Practice
                </h3>

                <p>

                    Students grow in a supportive environment
                    through interactive activities, guided
                    speaking exercises, and practice debates.

                </p>

            </div>


            <div class="card">

                <div class="number">
                    03
                </div>

                <h3>
                    Debate
                </h3>

                <p>

                    Students put their skills into action
                    through debate competitions that encourage
                    them to speak confidently, think on their
                    feet, and defend their ideas.

                </p>

            </div>


        </div>

    </div>

</section>



<!-- IMPACT -->

<section class="impact" id="impact">

    <div class="container impact-container">


        <div>

            <div class="big-number">

                100<span>+</span>

            </div>

            <div class="stat-label">

                STUDENTS EMPOWERED

            </div>

        </div>


        <div>

            <div class="eyebrow light">
                OUR IMPACT
            </div>

            <h2>

                More than debate.
                <br>
                Confidence for life.

            </h2>

            <p>

                Across our previous session groups,
                Debate Up has helped over 100 students
                become more confident in themselves
                through debate instruction, practice,
                and competitions.

            </p>

            <p>

                Our students are encouraged to step outside
                their comfort zones, speak in front of others,
                share their perspectives, think on their feet,
                and recognize the power of their own voice.

            </p>

            <p>

                The confidence students develop through debate
                can extend far beyond a competition. These skills
                can help students participate in class,
                communicate their ideas, become stronger leaders,
                and believe in their own abilities.

            </p>

        </div>


    </div>

</section>



<!-- STUDENT GROWTH -->

<section id="skills">

    <div class="container">

        <div class="eyebrow">
            WHAT STUDENTS GAIN
        </div>

        <h2>
            Skills that go beyond the podium.
        </h2>


        <div class="skill-grid">


            <div class="skill">

                <h3>
                    Confidence
                </h3>

                <p>

                    Develop the courage to speak in front
                    of others and confidently share ideas.

                </p>

            </div>


            <div class="skill">

                <h3>
                    Communication
                </h3>

                <p>

                    Learn to clearly express thoughts,
                    listen to others, and communicate
                    effectively.

                </p>

            </div>


            <div class="skill">

                <h3>
                    Critical Thinking
                </h3>

                <p>

                    Analyze topics, develop strong arguments,
                    and learn to respond thoughtfully.

                </p>

            </div>


            <div class="skill">

                <h3>
                    Leadership
                </h3>

                <p>

                    Learn to take initiative, advocate for
                    ideas, and grow into a stronger leader.

                </p>

            </div>


        </div>

    </div>

</section>



<!-- GET INVOLVED -->

<section class="cream" id="get-involved">

    <div class="container">

        <div class="eyebrow">
            GET INVOLVED
        </div>

        <h2>
            Be part of Debate Up.
        </h2>

        <p>

            Whether you are a student interested in developing
            your confidence, a volunteer who wants to make an
            impact, or someone interested in joining our team,
            there is a place for you at Debate Up.

        </p>


        <div class="cards">


            <!-- PROGRAM INFORMATION -->

            <div class="card">

                <h3>
                    Join Our Program
                </h3>

                <p>

                    Our programs are designed for students
                    in grades 6–8 who want to become more
                    confident speakers and develop their
                    debate and communication skills.

                </p>

                <a
                href="mailto:youth.for.literacy@gmail.com"
                class="application-link">

                    PROGRAM INFORMATION →

                </a>

            </div>


            <!-- VOLUNTEER -->

            <div class="card">

                <h3>
                    Volunteer Sign-Up
                </h3>

                <p>

                    Help Debate Up empower young students
                    and support our programs, sessions,
                    competitions, and mission.

                </p>

                <a
                href="https://gformsapp.com/f/1z_qWCErbraDI3NgN0K--UyWf_PSIrdB3r8EyqKV4vbc/en"
                target="_blank"
                class="application-link">

                    VOLUNTEER WITH US →

                </a>

            </div>


            <!-- OFFICER APPLICATION -->

            <div class="card">

                <h3>
                    Officer Application
                </h3>

                <p>

                    Interested in taking on a leadership
                    role and helping Debate Up continue
                    to grow? Apply to become part of
                    our team.

                </p>

                <a
                href="https://forms.gle/qNpVuL9j8K1zCvz17"
                target="_blank"
                class="application-link">

                    APPLY FOR A POSITION →

                </a>

            </div>


        </div>

    </div>

</section>



<!-- CONTACT -->

<section class="contact" id="contact">

    <div class="container">

        <div class="contact-content">

            <div class="eyebrow light">
                CONTACT US
            </div>

            <h2>
                Let's start a conversation.
            </h2>

            <p>

                Have a question about Debate Up,
                our programs, volunteering, applications,
                or getting involved?

                Reach out to our team to learn more.

            </p>

            <a
            href="mailto:youth.for.literacy@gmail.com"
            class="email-button">

                youth.for.literacy@gmail.com

            </a>

        </div>

    </div>

</section>



<!-- FOOTER -->

<footer>

    <h3>
        DEBATE UP
    </h3>

    <p>

        Empowering students in grades 6–8 through
        confidence, communication, and debate.

    </p>

    <p>
        501(c)(3) Nonprofit Organization
    </p>

</footer>


</body>
</html>
"""


@app.route("/")
def home():
    return HTML


if __name__ == "__main__":
    app.run(debug=True)