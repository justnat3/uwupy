from pyowo import CustomUwU
import json


class HttpUwU(Exception):

    def uwuHttpError(self, status_code):
        exception = "n_" + str(status_code)
        if status_code is None:
            raise CustomUwU("Status_Code param", "Ooops!", "Needs a big strong error_code")

        try:
            method = getattr(self, exception)
        except AttributeError:
            raise CustomUwU("Status_Code param", "o̲wo̲", "I missed that one... Sorry Senpai")

        return method()

    # : Info Responses
    def n_100(self):
        return(json.dumps({100: "UwU Keep going.."}))

    # : n_2XX Success
    def n_200(self):
        return(json.dumps({200: "(U ᵕ U❁) Reqwest was a Suckess"}))

    def n_201(self):
        return(json.dumps({201: "ᕦ( ˘ᴗ˘ )ᕤ Reswource Cweated just for you OwO"}))

    def n_202(self):
        return(json.dumps({202: "(⁄˘⁄⁄ω⁄⁄˘⁄)♡ Your reqwest was accepted Senpai"}))

    def n_204(self):
        return(json.dumps({204: "(°﹏°) You saw nothing!"}))

    def n_226(self):
        return(json.dumps({226: "OuO I am curwently being used Senpai"}))

    # :def n_3XX redirection

    def n_301(self):
        return(json.dumps({301: "owO oh.. sowwy.. The code monkeys have moved me permanently"}))

    def n_302(self):
        return(json.dumps({302: "uw- Oopsie! You've fwound me!"}))

    def n_304(self):
        return(json.dumps({304: "UwU Don't worwy I weft this one alone for you."}))

    # :def n_4XX Client Errors

    def n_400(self):
        return(json.dumps({400: "ღ(O꒳Oღ) RawR! Fucky Wucky Request."}))

    def n_401(self):
        return(json.dumps({401: "Oooh. You're not suppose to be here... Its not what it looks like uwu"}))

    def n_403(self):
        return(json.dumps({402: "(°꒳°) GWET OUT! The door was supposed to be locked!"}))

    def n_404(self):
        return(json.dumps({403: "UwU Emptwy Fiwwelds. Nothingness"}))

    def n_405(self):
        return(json.dumps({405: "𝒪𝓌𝒪 -Senpai! Are you sure this is the right way?"}))

    def n_409(self):
        return(json.dumps({406: "WONG HOLE -W-"}))

    def n_418(self):
        return ("I am a teapot... (*´∀｀)_旦",)

    def n_429(self):
        return(json.dumps({429: "End of the line OwO"}))

    # :def n_5XX Server Errors

    def n_500(self):
        return(json.dumps({500: "UwU My insides are messy"}))

    def n_501(self):
        return(json.dumps({501: "Not Compweted"}))

    def n_502(self):
        return(json.dumps({502: "Sowwy we couldn't find what your were looking for"}))

    def n_503(self):
        return(json.dumps({503: "Sowwy our code monkeys are working vewy hard to fix this"}))
