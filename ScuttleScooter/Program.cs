using Discord;
using Discord.WebSocket;
using System;
using ScuttleClasses;
using Discord.Commands;
// MTEyNjMzNjgwMTM4NTIzMDQyNw.GTZInu.-MwPSM5wdMrB8JOfsfJbvohkkpRoxUUyoZ_JLY
namespace ScuttleScooter 
{
    public class Program
    {
        public static Task Main(string[] args) => new Program().MainAsync();

        private static DiscordSocketClient _client;
        private static CommandService _commands;

        private CommandHandler commandHandler;

        public async Task MainAsync()
        {
            _client = new DiscordSocketClient();
            _commands = new CommandService();

            commandHandler = new CommandHandler(_client, _commands);
            await commandHandler.InstallCommandsAsync();

            _client.Log += Log;




            var token = "MTEyNjMzNjgwMTM4NTIzMDQyNw.GTZInu.-MwPSM5wdMrB8JOfsfJbvohkkpRoxUUyoZ_JLY";

            await _client.LoginAsync(TokenType.Bot, token);
            await _client.StartAsync();

            await Task.Delay(-1);
        }

        private Task Log(LogMessage msg)
        {
            Console.WriteLine(msg.ToString());
            return Task.CompletedTask;
        }

    }

}