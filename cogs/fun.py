from discord import Embed
from discord.ext.commands import Cog, command
from random import randint
from json import loads
from requests import get

class Fun(Cog):
    def __init__(self, client):
        self.client = client

    async def send_post(self, text):
        data = loads(text)['data']
        count = int(data['dist'])

        post = data['children'][randint(1, count)]['data']
        imageUrl = post['url_overridden_by_dest']
        title = post['title']
        image = Embed(title=title)
        image.set_image(url=imageUrl)
        
        return image

    @command(brief='Random waifu.')
    async def waifu(self, ctx):
        image = Embed()
        image.set_image(url=f'https://www.thiswaifudoesnotexist.net/example-{randint(0, 100000)}.jpg')

        await ctx.send(embed=image)
        
    @command(brief='red panda!')
    async def panda(self, ctx):
        try:
            image = Embed()
            imageUrl = loads(get('https://some-random-api.ml/img/red_panda').text)['link']
            image.set_image(url=imageUrl)

            await ctx.send(embed=image)
        except:
            await ctx.send("No panda :(")
            
    @command(brief='random anime drawing')
    async def anime(self, ctx):
        try:
            res = get('https://json.reddit.com/r/AnimeDrawings/hot/?sort=hot', headers={'User-Agent': 'Mozilla/5.0'})
            
            await ctx.send(embed=send_post(res.text))
        except:
            await ctx.send('no anime')

    @command(brief='random meme')
    async def meme(self, ctx):
        try:
            res = get('https://json.reddit.com/r/memes/hot/?sort=hot', headers={'User-Agent': 'Mozilla/5.0'})

            await ctx.send(embed=send_post(res.text))
        except:
            await ctx.send('No meme :(')

    @command(brief='djungelskog!')
    async def djungelskog(self, ctx):
        try:
            res = get('https://json.reddit.com/r/Djungelskog/hot/?sort=hot', headers={'User-Agent': 'Mozilla/5.0'})
            
            await ctx.send(embed=send_post(res.text))
        except:
            await ctx.send('No djungelskog :(')  

    @command(brief='shoob :)')
    async def shoob(self, ctx):
        try:
            imageUrl = loads(get('https://dog.ceo/api/breed/samoyed/images/random').text)['message']

            image = Embed()
            image.set_image(url=imageUrl)

            await ctx.send(embed=image)
        except:
            await ctx.send("No shoob :(")

    @command(brief='No anime.')
    async def noanime(self, ctx):
        await ctx.send('https://i.kym-cdn.com/entries/icons/original/000/027/108/anime.jpg')
    
    @command(brief='random.')
    async def randomcmd(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=63qtYi1nwcs')
        
    @command(brief='Ping!')
    async def ping(self, ctx):
        await ctx.send(f'pong!\n{round(self.client.latency * 1000)}ms')

    @command(brief='Lyne.')
    async def lyne(self, ctx):
        await ctx.send('http://www.risk-uk.com/wp-content/uploads/2015/04/JamesLyneSANSCyberAcademy1.png')

    @command(brief='Github.')
    async def github(self, ctx):
        await ctx.send('https://github.com/RealJammy/The-Jambot/blob/master/README.md')

    @command(brief='No leaking!!!')
    async def noleek(self, ctx):
        await ctx.send('https://game.joincyberdiscovery.com/assets/videos/cheating_message.mp4?version=4.2.0')
        
    @command(brief='uwu')
    async def uwu(self, ctx):
        await ctx.send('uwu!')

    @command(brief='scream! Only works on PC/ Desktop.')
    async def scream(self, ctx):
        await ctx.send('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', tts=True)
        
    @command(brief='ping pig')
    async def pingpig(self, ctx, amount=1):
        await ctx.send('<@295440396006326272>')
        await ctx.channel.purge(limit=amount + 1)
 
    @command(brief='Slough Song')
    async def slough(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=nwMK2ywRF78')
            
    @command(brief='to nag rag')
    async def nagrag(self, ctx):
        await ctx.send('Hey <@624713824087572480> this is a nag')
     
    @command(brief='to make das fuck off')
    async def fuckoffdas(self, ctx):
        await ctx.send('Hey <@695222074192429136> fuck off')
        
    @command(brief='To force JSnerd to get some sleep')
    async def jsnerd(self, ctx):
        await ctx.send('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa <@386245767725056015> get some sleep', tts=True)
        
        user = 386245767725056015
        await self.client.send_message(user, "fucking sleep ben ffs")

def setup(client):
    client.add_cog(Fun(client))
