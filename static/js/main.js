// 都道府県フィルタ機能
function filterByPrefecture() {
    const prefectureSelect = document.getElementById('prefecture-filter');
    const selectedPrefecture = prefectureSelect.value;
    
    // URLのクエリパラメータを更新してページをリロード
    const url = new URL(window.location);
    if (selectedPrefecture) {
        url.searchParams.set('prefecture', selectedPrefecture);
    } else {
        url.searchParams.delete('prefecture');
    }
    
    // ページをリロード（サーバーサイドフィルタリング）
    window.location.href = url.toString();
}

// ページ読み込み時の初期化
document.addEventListener('DOMContentLoaded', function() {
    // テーブル行数をカウント
    updateStationCount();
    
    // テーブル行のホバー効果を強化
    const tableRows = document.querySelectorAll('.weather-table tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.01)';
            this.style.transition = 'all 0.2s ease';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
    
    // 降水量データのアニメーション
    const rainValues = document.querySelectorAll('.rain-value.has-rain');
    rainValues.forEach(value => {
        value.addEventListener('click', function() {
            this.style.animation = 'none';
            setTimeout(() => {
                this.style.animation = 'pulse 1s ease-in-out';
            }, 10);
        });
    });
});

// 観測所数の更新
function updateStationCount() {
    const tableRows = document.querySelectorAll('.weather-table tbody tr');
    const totalCount = document.getElementById('total-count');
    if (totalCount) {
        totalCount.textContent = tableRows.length;
    }
}

// キーボードショートカット
document.addEventListener('keydown', function(event) {
    // Escキーでフィルタをクリア
    if (event.key === 'Escape') {
        const prefectureSelect = document.getElementById('prefecture-filter');
        prefectureSelect.value = '';
        filterByPrefecture();
    }
});

// レスポンシブテーブル機能
function handleResponsiveTable() {
    const table = document.querySelector('.weather-table');
    const container = document.querySelector('.table-container');
    
    if (window.innerWidth < 768) {
        container.style.overflowX = 'auto';
    } else {
        container.style.overflowX = 'visible';
    }
}

// ウィンドウサイズ変更時の処理
window.addEventListener('resize', handleResponsiveTable);
window.addEventListener('load', handleResponsiveTable);