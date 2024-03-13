import * as BABYLON from 'babylonjs'

var canvas = document.getElementById("renderCanvas");
var engine = new BABYLON.Engine(canvas, true);
var createScene  = function() {
   var scene = new BABYLON.Scene(engine);
   // Light
   var spot = new BABYLON.PointLight("spot", new BABYLON.Vector3(0, 30, 10), scene);
   spot.diffuse = new BABYLON.Color3(1, 1, 1);
   spot.specular = new BABYLON.Color3(0, 0, 0);

   // Camera
   var camera = new BABYLON.ArcRotateCamera("Camera", 0, 0.8, 100, BABYLON.Vector3.Zero(), scene);
   camera.lowerBetaLimit = 0.1;
   camera.upperBetaLimit = (Math.PI / 2) * 0.9;
   camera.lowerRadiusLimit = 30;
   camera.upperRadiusLimit = 150;
   camera.attachControl(canvas, true);

   // Ground
   var groundMaterial = new BABYLON.StandardMaterial("ground", scene);

   var ground = BABYLON.Mesh.CreateGroundFromHeightMap("ground", "heightmap.jpg", 200, 200, 250, 0, 10, scene, false);
   ground.material = groundMaterial;
   ground.material.wireframe = true;
   return scene;
};
var scene = createScene();
engine.runRenderLoop(function() {
   scene.render();
});