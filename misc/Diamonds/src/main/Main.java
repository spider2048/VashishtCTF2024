package main;

import java.io.IOException;
import java.util.Random;

import net.morbz.minecraft.blocks.DoorBlock;
import net.morbz.minecraft.blocks.Material;
import net.morbz.minecraft.blocks.SimpleBlock;
import net.morbz.minecraft.blocks.DoorBlock.DoorMaterial;
import net.morbz.minecraft.blocks.DoorBlock.HingeSide;
import net.morbz.minecraft.blocks.states.Facing4State;
import net.morbz.minecraft.level.FlatGenerator;
import net.morbz.minecraft.level.GameType;
import net.morbz.minecraft.level.IGenerator;
import net.morbz.minecraft.level.Level;
import net.morbz.minecraft.world.DefaultLayers;
import net.morbz.minecraft.world.World;

public class Main {
	// 13210031
	public static void main(String[] args) throws IOException {
		DefaultLayers layers = new DefaultLayers();
		IGenerator generator = new FlatGenerator(layers);
		
		Level level = new Level("MelonWorld", generator);
		level.setGameType(GameType.CREATIVE);
		level.setSpawnPoint(50, 256, 50);
		level.setAllowCommands(true);

		
		World world = new World(level, layers);
		Random rnd = new Random();
		
		int diamonds = 0;
		
		for(int x = 0; x < 500; x++) {
			for(int z = 0; z < 500; z++) {
				for(int y = 10; y < 256; y++) {
					if (rnd.nextInt(256) > 200) {
						diamonds++;
						world.setBlock(x, y, z, SimpleBlock.DIAMOND_BLOCK);
					} else {
						world.setBlock(x, y, z, SimpleBlock.AIR);	
					}
				}
			}
		}
		
		
		System.out.println("Diamonds:" + diamonds);
		world.save();
	}

}
