<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Register | NeedLink</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-900 via-blue-800 to-teal-700 text-gray-100 font-[Poppins]">

  <div class="bg-white/10 backdrop-blur-lg p-8 rounded-2xl shadow-2xl w-full max-w-md border border-white/20">
    <div class="text-center mb-6">
      <h1 class="text-3xl font-bold text-white tracking-wide">Create Account</h1>
      <p class="text-gray-300 text-sm mt-2">Join <span class="text-teal-400 font-semibold">NeedLink</span> today</p>
    </div>

    <form method="POST" class="space-y-4">
      {% csrf_token %}
      <div>
        <label for="username" class="block text-sm mb-1 text-gray-200">Username</label>
        <input type="text" id="username" name="username" required
               class="w-full px-4 py-2 rounded-lg bg-white/20 text-white placeholder-gray-300 focus:ring-2 focus:ring-teal-400 focus:outline-none">
      </div>

      <div>
        <label for="email" class="block text-sm mb-1 text-gray-200">Email</label>
        <input type="email" id="email" name="email" required
               class="w-full px-4 py-2 rounded-lg bg-white/20 text-white placeholder-gray-300 focus:ring-2 focus:ring-teal-400 focus:outline-none">
      </div>

      <div>
        <label for="password" class="block text-sm mb-1 text-gray-200">Password</label>
        <input type="password" id="password" name="password" required
               class="w-full px-4 py-2 rounded-lg bg-white/20 text-white placeholder-gray-300 focus:ring-2 focus:ring-teal-400 focus:outline-none">
      </div>

      <button type="submit"
              class="w-full py-2 mt-4 bg-gradient-to-r from-blue-600 to-teal-500 rounded-lg shadow-md hover:shadow-xl transition duration-300 font-semibold text-white">
        Register
      </button>

      <p class="text-sm text-center text-gray-300 mt-3">
        Already have an account?
        <a href="{% url 'login_page' %}" class="text-teal-400 hover:text-teal-300 font-medium">Login</a>
      </p>
    </form>
  </div>

  <footer class="absolute bottom-4 text-xs text-gray-300 opacity-80">
    Powered by <span class="font-semibold text-white">DevniFy Devs</span>
  </footer>

</body>
</html>











/////////////////////////////////////////////////////////////////////////////////////////////////









<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login | NeedLink</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-900 via-blue-800 to-teal-700 text-gray-100 font-[Poppins]">

  <div class="bg-white/10 backdrop-blur-lg p-8 rounded-2xl shadow-2xl w-full max-w-md border border-white/20">
    <div class="text-center mb-6">
      <h1 class="text-3xl font-bold text-white tracking-wide">Welcome Back</h1>
      <p class="text-gray-300 text-sm mt-2">Login to your <span class="text-teal-400 font-semibold">NeedLink</span> account</p>
    </div>

    <form method="POST" class="space-y-4">
      {% csrf_token %}
      <div>
        <label for="username" class="block text-sm mb-1 text-gray-200">Username</label>
        <input type="text" id="username" name="username" required
               class="w-full px-4 py-2 rounded-lg bg-white/20 text-white placeholder-gray-300 focus:ring-2 focus:ring-teal-400 focus:outline-none">
      </div>

      <div>
        <label for="password" class="block text-sm mb-1 text-gray-200">Password</label>
        <input type="password" id="password" name="password" required
               class="w-full px-4 py-2 rounded-lg bg-white/20 text-white placeholder-gray-300 focus:ring-2 focus:ring-teal-400 focus:outline-none">
      </div>

      <button type="submit"
              class="w-full py-2 mt-4 bg-gradient-to-r from-blue-600 to-teal-500 rounded-lg shadow-md hover:shadow-xl transition duration-300 font-semibold text-white">
        Login
      </button>

      <p class="text-sm text-center text-gray-300 mt-3">
        Don’t have an account?
        <a href="{% url 'register_page' %}" class="text-teal-400 hover:text-teal-300 font-medium">Register</a>
      </p>
    </form>
  </div>

  <footer class="absolute bottom-4 text-xs text-gray-300 opacity-80">
    Powered by <span class="font-semibold text-white">DevniFy Devs</span>
  </footer>

</body>
</html>








////////////////////////////////////////////////////////////////////////////////////////




