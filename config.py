from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 10248430
    API_HASH = "42396a6ff14a569b9d59931643897d0d"
    # the name to display in your alive message
    ALIVE_NAME = "rishabh"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://hwtxqqfc:U_QHjE6TByrb8MVJOuEcfDod9FXa1BkN@satao.db.elephantsql.com/hwtxqqfc"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOGgBu21dLz241cIdffngb3vF5b400tG2ARIv9j48fNjbCn_HLblpx8UeAyzUNsR7RPjx3z_QNbDHfGgsyRYQe7EMwJ8HhHUGbjJuVbHAomifZuIFoPFEYbngy0pHRgyMQylOg4iYIInczI0onBnoeK-7PfbD0mLU3EHrV8D87UgbgrK7jKpajOPJ0sM5RfG5C1AVP__6UErvqy65B23Z-CS5wWRiuMpvMEI9-bsalbqeMleorC49tycwOC0Ab1e5WOteqKS-S0grhBWFXubc6QNYDLW_3VxJFWOkAU6sxG9IlMoBH2KQ8ERKeaeLxOCKK0VkqyFnvTyWSMSbWCrClwvZM4M="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5509473272:AAEXFx2yPYrY_KvL4B9lrn3Zh0jzhJWPaBs"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001623978356
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/rishabhanand2/tha_plugins"
    #don't edit this 
    THANOSABUSE = "False"#don't edit this
