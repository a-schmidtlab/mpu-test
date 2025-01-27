let scene, camera, renderer, cube;
let currentRotation = { x: 0, y: 0, z: 0 };

function init() {
    // Create scene
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Create cube
    const geometry = new THREE.BoxGeometry(2, 0.2, 1);
    const material = new THREE.MeshPhongMaterial({ color: 0x00ff00 });
    cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    // Add lights
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(1, 1, 1);
    scene.add(light);
    scene.add(new THREE.AmbientLight(0x404040));

    // Position camera
    camera.position.z = 5;

    // Handle window resize
    window.addEventListener('resize', onWindowResize, false);
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function updateDataDisplay(data) {
    document.getElementById('acc-x').textContent = data.accelerometer.x.toFixed(2);
    document.getElementById('acc-y').textContent = data.accelerometer.y.toFixed(2);
    document.getElementById('acc-z').textContent = data.accelerometer.z.toFixed(2);
    document.getElementById('gyro-x').textContent = data.gyroscope.x.toFixed(2);
    document.getElementById('gyro-y').textContent = data.gyroscope.y.toFixed(2);
    document.getElementById('gyro-z').textContent = data.gyroscope.z.toFixed(2);
}

function animate() {
    requestAnimationFrame(animate);

    // Smooth rotation transition
    cube.rotation.x = currentRotation.x;
    cube.rotation.y = currentRotation.y;
    cube.rotation.z = currentRotation.z;

    renderer.render(scene, camera);
}

function fetchData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            updateDataDisplay(data);
            
            // Convert accelerometer data to rotation
            currentRotation.x = Math.atan2(data.accelerometer.y, data.accelerometer.z);
            currentRotation.y = Math.atan2(data.accelerometer.x, data.accelerometer.z);
            currentRotation.z = Math.atan2(data.accelerometer.y, data.accelerometer.x);
        })
        .catch(error => console.error('Error fetching sensor data:', error));
}

// Initialize the scene
init();
animate();

// Fetch sensor data every 100ms
setInterval(fetchData, 100); 