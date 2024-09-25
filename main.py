#Written By :  Nill
#Date       :  09/26/2024
#Version    :  1.0
#==============================
import re
import os
import time
import requests
from rich.console import Console
from rich.tree import Tree
from rich.panel import Panel

console = Console()
fileName1 = 'HighRich - ' + time.strftime("%Y-%m-%d   %H-%M-%S") + '.txt'
fileName2 = 'LowRich - ' + time.strftime("%Y-%m-%d   %H-%M-%S") + '.txt'
def __HighRich__(guid, posts):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'dpr': '1',
        'priority': 'u=0, i',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'viewport-width': '1365',
    }
    try:
        response = requests.get(f'https://www.facebook.com/groups/{guid}/about', headers=headers)
        if response.status_code != 200:
            console.print(f"[red]Failed to access group {guid}: {response.status_code}[/red]")
            return
        response_text = response.text
        facebook_posts = re.search(r'number_of_posts_in_last_day["\']:\s*(\d+)', response_text)
        total_members = re.search(r'group_total_members_info_text["\']:\s*["\']([^"\']+)["\']', response_text).group(1).replace('total members','')
        __GNAME__ = re.findall(r'"Group","name":"(.*?)"', response_text)[0]
        Gname = 'Name Error' if '\\u' in __GNAME__ else __GNAME__
        if facebook_posts:
            facebook_posts = int(facebook_posts.group(1))
            if facebook_posts >= int(posts):
                tree = Tree(f"Group :[bold sea_green2] https://www.facebook.com/groups/{guid}")
                __1X__ = tree.add(f"[plum2]Group Name :[orange_red1] {Gname}")
                __1X__.add(f"[plum2]Total Members :[bold sea_green2] {total_members}")
                __1X__.add(f"[plum2]New Posts Today :[bold sea_green2] {facebook_posts}")
                panel = Panel(tree, width=90, border_style="cyan2", title="[bold bright_green]High Rich")
                console.print(panel)
                with open(fileName1,"a") as file:
                    file.write(f"https://www.facebook.com/groups/{guid}\n")
            else:
                tree = Tree(f"[violet]Group :[bold deep_pink2] https://www.facebook.com/groups/{guid}")
                __1X__ = tree.add(f"[violet]Group Name :[bold deep_pink2] {Gname}")
                __1X__.add(f"[violet]Total Members :[bold deep_pink2] {total_members}")
                __1X__.add(f"[violet]New Posts Today :[bold deep_pink2] {facebook_posts}")
                panel = Panel(tree, width=90, border_style="dark_violet", title="Low Rich")
                console.print(panel)
                with open(fileName2,"a") as file:
                    file.write(f"https://www.facebook.com/groups/{guid}\n")
        else:
            console.print(f"[red]Unable to retrieve posts for Group {guid}.[/red]")
    except Exception as e:      
        tree = Tree(f"Group :[red] https://www.facebook.com/groups/{guid}")
        __1X__ = tree.add(f"Group Name :[red] Error 404 Not Found")
        __1X__.add(f"Total Members :[red] Error 404 Not Found")
        __1X__.add(f"New Posts Today :[red] Error 404 Not Found")
        panel = Panel(tree, width=90, border_style="red", title="Error")
        console.print(panel)

def check_groups_from_file(posts):
    with open('Group_Uids.txt', 'r') as file:
        group_ids = file.readlines()
    group_ids = [group_id.strip() for group_id in group_ids if group_id.strip()]
    for group_id in group_ids:
        __HighRich__(group_id, posts)
        time.sleep(2)
def banner():
    os.system('cls')
    console.print(Panel(f"""[bold gold1]        ╦ ╦╦╔═╗╦ ╦  ╦═╗╦╔═╗╦ ╦  ╔═╗╦═╗╔═╗╦ ╦╔═╗  ╔═╗╦ ╔╗╔╔╦╗╔═╗╦═╗
        ╠═╣║║ ╦╠═╣  ╠╦╝║║  ╠═╣  ║ ╦╠╦╝║ ║║ ║╠═╝  ╠╣ ║ ║║║ ║║║╣ ╠╦╝
        ╩ ╩╩╚═╝╩ ╩  ╩╚═╩╚═╝╩ ╩  ╚═╝╩╚═╚═╝╚═╝╩    ╚  ╩ ╝╚╝═╩╝╚═╝╩╚═""",width=90,padding=(0,8),style=f"bold white",title=f"NILL-XD"))
if __name__=='__main__':
    banner()
    posts = input('Posts Per Day => ')
    banner()
    check_groups_from_file(posts)
