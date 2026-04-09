import * as React from "react"

const Button = React.forwardRef(({ className = "", variant = "default", size = "default", ...props }, ref) => {
  const variants = {
    default: "bg-brand-navy text-white hover:bg-brand-navy/90",
    destructive: "bg-red-500 text-white hover:bg-red-500/90",
    outline: "border border-gray-300 bg-white hover:bg-gray-100",
    secondary: "bg-brand-gold text-white hover:bg-brand-gold/80",
    ghost: "hover:bg-gray-100",
    link: "text-brand-navy underline-offset-4 hover:underline",
  }
  
  const sizes = {
    default: "h-10 px-4 py-2",
    sm: "h-9 rounded-md px-3",
    lg: "h-11 rounded-md px-8",
    icon: "h-10 w-10",
  }

  return (
    <button
      className={`inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 ${variants[variant]} ${sizes[size]} ${className}`}
      ref={ref}
      {...props}
    />
  )
})
Button.displayName = "Button"

export { Button }
