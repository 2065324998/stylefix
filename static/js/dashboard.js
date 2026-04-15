/**
 * Dashboard interactivity — sidebar toggle, modal, toast notifications.
 */

document.addEventListener("DOMContentLoaded", function () {

    // --- Sidebar toggle ---
    var menuBtn = document.querySelector('[data-action="toggle-sidebar"]');
    var sidebar = document.querySelector(".sidebar");
    if (menuBtn && sidebar) {
        menuBtn.addEventListener("click", function () {
            sidebar.classList.toggle("sidebar--collapsed");
        });
    }

    // --- Modal open/close ---
    document.querySelectorAll('[data-action="open-modal"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            var modal = document.getElementById("detail-modal");
            if (modal) {
                modal.classList.add("active");
            }
        });
    });

    document.querySelectorAll('[data-action="close-modal"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            var modal = document.getElementById("detail-modal");
            if (modal) {
                modal.classList.remove("active");
            }
        });
    });

    // Close modal on overlay click
    var modalOverlay = document.getElementById("detail-modal");
    if (modalOverlay) {
        modalOverlay.addEventListener("click", function (e) {
            if (e.target === modalOverlay) {
                modalOverlay.classList.remove("active");
            }
        });
    }

    // --- Toast notifications ---
    document.querySelectorAll('[data-action="show-toast"]').forEach(function (btn) {
        btn.addEventListener("click", function () {
            showToast("Action completed successfully");
        });
    });

    // --- Scroll to top ---
    var contentArea = document.getElementById("content");
    if (contentArea) {
        var scrollTopBtn = document.querySelector('[data-action="scroll-top"]');
        if (scrollTopBtn) {
            scrollTopBtn.addEventListener("click", function () {
                contentArea.scrollTo({ top: 0, behavior: "smooth" });
            });
        }
    }

    // --- Content area width tracking (for responsive breakpoints) ---
    function updateContentWidth() {
        var content = document.getElementById("content");
        if (content) {
            var width = content.offsetWidth;
            content.setAttribute("data-width",
                width < 600 ? "narrow" : width < 1000 ? "medium" : "wide"
            );
        }
    }
    updateContentWidth();
    window.addEventListener("resize", updateContentWidth);
});


function showToast(message) {
    var container = document.getElementById("toast-container");
    if (!container) return;

    var toast = document.createElement("div");
    toast.className = "toast";
    toast.textContent = message;
    container.appendChild(toast);

    setTimeout(function () {
        toast.style.opacity = "0";
        toast.style.transition = "opacity 0.3s ease";
        setTimeout(function () {
            toast.remove();
        }, 300);
    }, 4000);
}
