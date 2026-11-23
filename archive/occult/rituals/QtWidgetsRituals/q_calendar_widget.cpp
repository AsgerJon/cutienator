//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcalendarwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcalendarwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qcalendar.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QCalendarWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCalendarWidget : QCalendarWidget {
  using QCalendarWidget::event;
  using QCalendarWidget::eventFilter;
  using QCalendarWidget::mousePressEvent;
  using QCalendarWidget::resizeEvent;
  using QCalendarWidget::keyPressEvent;
  using QCalendarWidget::paintCell;
};

//  A QCalendarWidget that Python can take functions over in. Every QCalendarWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQCalendarWidgetCall0)(const void *, int *);
typedef const QSize * (*CuteQCalendarWidgetCall1)(const void *, int *);
typedef bool (*CuteQCalendarWidgetCall2)(const void *, QEvent *, int *);
typedef bool (*CuteQCalendarWidgetCall3)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQCalendarWidgetCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCalendarWidgetCall5)(const void *, QResizeEvent *, int *);
typedef void (*CuteQCalendarWidgetCall6)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCalendarWidgetCall7)(const void *, QPainter *, const QRect *, const QDate *, int *);
typedef int (*CuteQCalendarWidgetCall8)(const void *, int *);
typedef void (*CuteQCalendarWidgetCall9)(const void *, bool, int *);
typedef int (*CuteQCalendarWidgetCall10)(const void *, int, int *);
typedef bool (*CuteQCalendarWidgetCall11)(const void *, int *);
typedef void * (*CuteQCalendarWidgetCall12)(const void *, int *);
typedef void (*CuteQCalendarWidgetCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCalendarWidgetCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCalendarWidgetCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQCalendarWidgetCall16)(const void *, QWheelEvent *, int *);
typedef void (*CuteQCalendarWidgetCall17)(const void *, QKeyEvent *, int *);
typedef void (*CuteQCalendarWidgetCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCalendarWidgetCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQCalendarWidgetCall20)(const void *, QEnterEvent *, int *);
typedef void (*CuteQCalendarWidgetCall21)(const void *, QEvent *, int *);
typedef void (*CuteQCalendarWidgetCall22)(const void *, QPaintEvent *, int *);
typedef void (*CuteQCalendarWidgetCall23)(const void *, QMoveEvent *, int *);
typedef void (*CuteQCalendarWidgetCall24)(const void *, QCloseEvent *, int *);
typedef void (*CuteQCalendarWidgetCall25)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQCalendarWidgetCall26)(const void *, QTabletEvent *, int *);
typedef void (*CuteQCalendarWidgetCall27)(const void *, QActionEvent *, int *);
typedef void (*CuteQCalendarWidgetCall28)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQCalendarWidgetCall29)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQCalendarWidgetCall30)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQCalendarWidgetCall31)(const void *, QDropEvent *, int *);
typedef void (*CuteQCalendarWidgetCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQCalendarWidgetCall33)(const void *, QHideEvent *, int *);
typedef void (*CuteQCalendarWidgetCall34)(const void *, QEvent *, int *);
typedef int (*CuteQCalendarWidgetCall35)(const void *, int, int *);
typedef void (*CuteQCalendarWidgetCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQCalendarWidgetCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQCalendarWidgetCall38)(const void *, int *);
typedef void (*CuteQCalendarWidgetCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQCalendarWidgetCall40)(const void *, int, int *);
typedef bool (*CuteQCalendarWidgetCall41)(const void *, bool, int *);
typedef void (*CuteQCalendarWidgetCall42)(const void *, QTimerEvent *, int *);
typedef void (*CuteQCalendarWidgetCall43)(const void *, QChildEvent *, int *);
typedef void (*CuteQCalendarWidgetCall44)(const void *, QEvent *, int *);
typedef void (*CuteQCalendarWidgetCall45)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQCalendarWidgetCall46)(const void *, const QMetaMethod *, int *);
class CuteQCalendarWidget : public QCalendarWidget {
public:
  using QCalendarWidget::QCalendarWidget;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QCalendarWidget9paintCellEP8QPainterRK5QRect5QDate")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
    return false;
  }

  //  QSize QCalendarWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCalendarWidgetCall0 call = reinterpret_cast<CuteQCalendarWidgetCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCalendarWidget::sizeHint();
  }

  //  QSize QCalendarWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCalendarWidgetCall1 call = reinterpret_cast<CuteQCalendarWidgetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCalendarWidget::minimumSizeHint();
  }

  //  bool QCalendarWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCalendarWidgetCall2 call = reinterpret_cast<CuteQCalendarWidgetCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QCalendarWidget::event(event);
  }

  //  bool QCalendarWidget::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCalendarWidgetCall3 call = reinterpret_cast<CuteQCalendarWidgetCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QCalendarWidget::eventFilter(watched, event);
  }

  //  void QCalendarWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCalendarWidgetCall4 call = reinterpret_cast<CuteQCalendarWidgetCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QCalendarWidget::mousePressEvent(event);
  }

  //  void QCalendarWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCalendarWidgetCall5 call = reinterpret_cast<CuteQCalendarWidgetCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QCalendarWidget::resizeEvent(event);
  }

  //  void QCalendarWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCalendarWidgetCall6 call = reinterpret_cast<CuteQCalendarWidgetCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QCalendarWidget::keyPressEvent(event);
  }

  //  void QCalendarWidget::paintCell(QPainter *painter, const QRect &rect,
  //      QDate date) const
  void paintCell(
      QPainter *painter,
      const QRect &rect,
      QDate date) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCalendarWidgetCall7 call = reinterpret_cast<CuteQCalendarWidgetCall7>(taken[7]);
      call(this, painter, &rect, &date, &handled);
      if (handled) return;
    }
    QCalendarWidget::paintCell(painter, rect, date);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCalendarWidgetCall8 call = reinterpret_cast<CuteQCalendarWidgetCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCalendarWidgetCall9 call = reinterpret_cast<CuteQCalendarWidgetCall9>(taken[9]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQCalendarWidgetCall10 call = reinterpret_cast<CuteQCalendarWidgetCall10>(taken[10]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQCalendarWidgetCall11 call = reinterpret_cast<CuteQCalendarWidgetCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQCalendarWidgetCall12 call = reinterpret_cast<CuteQCalendarWidgetCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCalendarWidgetCall13 call = reinterpret_cast<CuteQCalendarWidgetCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCalendarWidgetCall14 call = reinterpret_cast<CuteQCalendarWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCalendarWidgetCall15 call = reinterpret_cast<CuteQCalendarWidgetCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQCalendarWidgetCall16 call = reinterpret_cast<CuteQCalendarWidgetCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQCalendarWidgetCall17 call = reinterpret_cast<CuteQCalendarWidgetCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQCalendarWidgetCall18 call = reinterpret_cast<CuteQCalendarWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQCalendarWidgetCall19 call = reinterpret_cast<CuteQCalendarWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQCalendarWidgetCall20 call = reinterpret_cast<CuteQCalendarWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQCalendarWidgetCall21 call = reinterpret_cast<CuteQCalendarWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQCalendarWidgetCall22 call = reinterpret_cast<CuteQCalendarWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQCalendarWidgetCall23 call = reinterpret_cast<CuteQCalendarWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQCalendarWidgetCall24 call = reinterpret_cast<CuteQCalendarWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQCalendarWidgetCall25 call = reinterpret_cast<CuteQCalendarWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQCalendarWidgetCall26 call = reinterpret_cast<CuteQCalendarWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQCalendarWidgetCall27 call = reinterpret_cast<CuteQCalendarWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQCalendarWidgetCall28 call = reinterpret_cast<CuteQCalendarWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQCalendarWidgetCall29 call = reinterpret_cast<CuteQCalendarWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQCalendarWidgetCall30 call = reinterpret_cast<CuteQCalendarWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQCalendarWidgetCall31 call = reinterpret_cast<CuteQCalendarWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQCalendarWidgetCall32 call = reinterpret_cast<CuteQCalendarWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQCalendarWidgetCall33 call = reinterpret_cast<CuteQCalendarWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQCalendarWidgetCall34 call = reinterpret_cast<CuteQCalendarWidgetCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQCalendarWidgetCall35 call = reinterpret_cast<CuteQCalendarWidgetCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQCalendarWidgetCall36 call = reinterpret_cast<CuteQCalendarWidgetCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQCalendarWidgetCall37 call = reinterpret_cast<CuteQCalendarWidgetCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQCalendarWidgetCall38 call = reinterpret_cast<CuteQCalendarWidgetCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQCalendarWidgetCall39 call = reinterpret_cast<CuteQCalendarWidgetCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQCalendarWidgetCall40 call = reinterpret_cast<CuteQCalendarWidgetCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQCalendarWidgetCall41 call = reinterpret_cast<CuteQCalendarWidgetCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQCalendarWidgetCall42 call = reinterpret_cast<CuteQCalendarWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQCalendarWidgetCall43 call = reinterpret_cast<CuteQCalendarWidgetCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQCalendarWidgetCall44 call = reinterpret_cast<CuteQCalendarWidgetCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQCalendarWidgetCall45 call = reinterpret_cast<CuteQCalendarWidgetCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQCalendarWidgetCall46 call = reinterpret_cast<CuteQCalendarWidgetCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QCalendarWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QCalendarWidget10metaObjectEv(
    const QCalendarWidget *self) {
  return self->metaObject();
}

//  QString QCalendarWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QCalendarWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCalendarWidget::tr(s, c, n));
}

//  QCalendarWidget::QCalendarWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QCalendarWidget *ritual_ZN15QCalendarWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQCalendarWidget(parent);
}

//  QCalendarWidget::~QCalendarWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidgetD1Ev(QCalendarWidget *self) {
  delete self;
}

//  QSize QCalendarWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QCalendarWidget8sizeHintEv(const QCalendarWidget *self) {
  return new QSize(self->sizeHint());
}

//  QSize QCalendarWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QCalendarWidget15minimumSizeHintEv(
    const QCalendarWidget *self) {
  return new QSize(self->minimumSizeHint());
}

//  QDate QCalendarWidget::selectedDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK15QCalendarWidget12selectedDateEv(
    const QCalendarWidget *self) {
  return new QDate(self->selectedDate());
}

//  int QCalendarWidget::yearShown() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCalendarWidget9yearShownEv(const QCalendarWidget *self) {
  return self->yearShown();
}

//  int QCalendarWidget::monthShown() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCalendarWidget10monthShownEv(const QCalendarWidget *self) {
  return self->monthShown();
}

//  QDate QCalendarWidget::minimumDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK15QCalendarWidget11minimumDateEv(
    const QCalendarWidget *self) {
  return new QDate(self->minimumDate());
}

//  void QCalendarWidget::setMinimumDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget14setMinimumDateE5QDate(
    QCalendarWidget *self,
    const QDate *date) {
  self->setMinimumDate(*date);
}

//  void QCalendarWidget::clearMinimumDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16clearMinimumDateEv(QCalendarWidget *self) {
  self->clearMinimumDate();
}

//  QDate QCalendarWidget::maximumDate() const
extern "C" Q_DECL_EXPORT
QDate *ritual_ZNK15QCalendarWidget11maximumDateEv(
    const QCalendarWidget *self) {
  return new QDate(self->maximumDate());
}

//  void QCalendarWidget::setMaximumDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget14setMaximumDateE5QDate(
    QCalendarWidget *self,
    const QDate *date) {
  self->setMaximumDate(*date);
}

//  void QCalendarWidget::clearMaximumDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16clearMaximumDateEv(QCalendarWidget *self) {
  self->clearMaximumDate();
}

//  Qt::DayOfWeek QCalendarWidget::firstDayOfWeek() const
extern "C" Q_DECL_EXPORT
Qt::DayOfWeek ritual_ZNK15QCalendarWidget14firstDayOfWeekEv(
    const QCalendarWidget *self) {
  return self->firstDayOfWeek();
}

//  void QCalendarWidget::setFirstDayOfWeek(Qt::DayOfWeek dayOfWeek)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget17setFirstDayOfWeekEN2Qt9DayOfWeekE(
    QCalendarWidget *self,
    Qt::DayOfWeek dayOfWeek) {
  self->setFirstDayOfWeek(dayOfWeek);
}

//  bool QCalendarWidget::isNavigationBarVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCalendarWidget22isNavigationBarVisibleEv(
    const QCalendarWidget *self) {
  return self->isNavigationBarVisible();
}

//  bool QCalendarWidget::isGridVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCalendarWidget13isGridVisibleEv(
    const QCalendarWidget *self) {
  return self->isGridVisible();
}

//  QCalendar QCalendarWidget::calendar() const
extern "C" Q_DECL_EXPORT
QCalendar *ritual_ZNK15QCalendarWidget8calendarEv(
    const QCalendarWidget *self) {
  return new QCalendar(self->calendar());
}

//  void QCalendarWidget::setCalendar(QCalendar calendar)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget11setCalendarE9QCalendar(
    QCalendarWidget *self,
    const QCalendar *calendar) {
  self->setCalendar(*calendar);
}

//  SelectionMode QCalendarWidget::selectionMode() const
extern "C" Q_DECL_EXPORT
QCalendarWidget::SelectionMode ritual_ZNK15QCalendarWidget13selectionModeEv(
    const QCalendarWidget *self) {
  return self->selectionMode();
}

//  void QCalendarWidget::setSelectionMode(SelectionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16setSelectionModeENS_13SelectionModeE(
    QCalendarWidget *self,
    QCalendarWidget::SelectionMode mode) {
  self->setSelectionMode(mode);
}

//  HorizontalHeaderFormat QCalendarWidget::horizontalHeaderFormat() const
extern "C" Q_DECL_EXPORT
QCalendarWidget::HorizontalHeaderFormat ritual_ZNK15QCalendarWidget22horizontalHeaderFormatEv(
    const QCalendarWidget *self) {
  return self->horizontalHeaderFormat();
}

//  void QCalendarWidget::setHorizontalHeaderFormat(HorizontalHeaderFormat
//      format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget25setHorizontalHeaderFormatENS_22HorizontalHeaderFormatE(
    QCalendarWidget *self,
    QCalendarWidget::HorizontalHeaderFormat format) {
  self->setHorizontalHeaderFormat(format);
}

//  VerticalHeaderFormat QCalendarWidget::verticalHeaderFormat() const
extern "C" Q_DECL_EXPORT
QCalendarWidget::VerticalHeaderFormat ritual_ZNK15QCalendarWidget20verticalHeaderFormatEv(
    const QCalendarWidget *self) {
  return self->verticalHeaderFormat();
}

//  void QCalendarWidget::setVerticalHeaderFormat(VerticalHeaderFormat
//      format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget23setVerticalHeaderFormatENS_20VerticalHeaderFormatE(
    QCalendarWidget *self,
    QCalendarWidget::VerticalHeaderFormat format) {
  self->setVerticalHeaderFormat(format);
}

//  QTextCharFormat QCalendarWidget::headerTextFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK15QCalendarWidget16headerTextFormatEv(
    const QCalendarWidget *self) {
  return new QTextCharFormat(self->headerTextFormat());
}

//  void QCalendarWidget::setHeaderTextFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget19setHeaderTextFormatERK15QTextCharFormat(
    QCalendarWidget *self,
    const QTextCharFormat *format) {
  self->setHeaderTextFormat(*format);
}

//  QTextCharFormat QCalendarWidget::weekdayTextFormat(Qt::DayOfWeek
//      dayOfWeek) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK15QCalendarWidget17weekdayTextFormatEN2Qt9DayOfWeekE(
    const QCalendarWidget *self,
    Qt::DayOfWeek dayOfWeek) {
  return new QTextCharFormat(self->weekdayTextFormat(dayOfWeek));
}

//  void QCalendarWidget::setWeekdayTextFormat(Qt::DayOfWeek dayOfWeek, const
//      QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget20setWeekdayTextFormatEN2Qt9DayOfWeekERK15QTextCharFormat(
    QCalendarWidget *self,
    Qt::DayOfWeek dayOfWeek,
    const QTextCharFormat *format) {
  self->setWeekdayTextFormat(dayOfWeek, *format);
}

//  QTextCharFormat QCalendarWidget::dateTextFormat(QDate date) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK15QCalendarWidget14dateTextFormatE5QDate(
    const QCalendarWidget *self,
    const QDate *date) {
  return new QTextCharFormat(self->dateTextFormat(*date));
}

//  void QCalendarWidget::setDateTextFormat(QDate date, const QTextCharFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget17setDateTextFormatE5QDateRK15QTextCharFormat(
    QCalendarWidget *self,
    const QDate *date,
    const QTextCharFormat *format) {
  self->setDateTextFormat(*date, *format);
}

//  bool QCalendarWidget::isDateEditEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCalendarWidget17isDateEditEnabledEv(
    const QCalendarWidget *self) {
  return self->isDateEditEnabled();
}

//  void QCalendarWidget::setDateEditEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget18setDateEditEnabledEb(
    QCalendarWidget *self,
    bool enable) {
  self->setDateEditEnabled(enable);
}

//  int QCalendarWidget::dateEditAcceptDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCalendarWidget19dateEditAcceptDelayEv(
    const QCalendarWidget *self) {
  return self->dateEditAcceptDelay();
}

//  void QCalendarWidget::setDateEditAcceptDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget22setDateEditAcceptDelayEi(
    QCalendarWidget *self,
    int delay) {
  self->setDateEditAcceptDelay(delay);
}

//  bool QCalendarWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QCalendarWidget5eventEP6QEvent(
    QCalendarWidget *self,
    QEvent *event) {
  return self->event(event);
}

//  bool QCalendarWidget::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QCalendarWidget11eventFilterEP7QObjectP6QEvent(
    QCalendarWidget *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  void QCalendarWidget::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget15mousePressEventEP11QMouseEvent(
    QCalendarWidget *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QCalendarWidget::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget11resizeEventEP12QResizeEvent(
    QCalendarWidget *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QCalendarWidget::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget13keyPressEventEP9QKeyEvent(
    QCalendarWidget *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QCalendarWidget::paintCell(QPainter *painter, const QRect &rect,
//      QDate date) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QCalendarWidget9paintCellEP8QPainterRK5QRect5QDate(
    const QCalendarWidget *self,
    QPainter *painter,
    const QRect *rect,
    const QDate *date) {
  self->paintCell(painter, *rect, *date);
}

//  void QCalendarWidget::updateCell(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget10updateCellE5QDate(
    QCalendarWidget *self,
    const QDate *date) {
  self->updateCell(*date);
}

//  void QCalendarWidget::updateCells()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget11updateCellsEv(QCalendarWidget *self) {
  self->updateCells();
}

//  void QCalendarWidget::setSelectedDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget15setSelectedDateE5QDate(
    QCalendarWidget *self,
    const QDate *date) {
  self->setSelectedDate(*date);
}

//  void QCalendarWidget::setDateRange(QDate min, QDate max)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget12setDateRangeE5QDateS0_(
    QCalendarWidget *self,
    const QDate *min,
    const QDate *max) {
  self->setDateRange(*min, *max);
}

//  void QCalendarWidget::setCurrentPage(int year, int month)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget14setCurrentPageEii(
    QCalendarWidget *self,
    int year,
    int month) {
  self->setCurrentPage(year, month);
}

//  void QCalendarWidget::setGridVisible(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget14setGridVisibleEb(
    QCalendarWidget *self,
    bool show) {
  self->setGridVisible(show);
}

//  void QCalendarWidget::setNavigationBarVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget23setNavigationBarVisibleEb(
    QCalendarWidget *self,
    bool visible) {
  self->setNavigationBarVisible(visible);
}

//  void QCalendarWidget::showNextMonth()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget13showNextMonthEv(QCalendarWidget *self) {
  self->showNextMonth();
}

//  void QCalendarWidget::showPreviousMonth()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget17showPreviousMonthEv(QCalendarWidget *self) {
  self->showPreviousMonth();
}

//  void QCalendarWidget::showNextYear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget12showNextYearEv(QCalendarWidget *self) {
  self->showNextYear();
}

//  void QCalendarWidget::showPreviousYear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16showPreviousYearEv(QCalendarWidget *self) {
  self->showPreviousYear();
}

//  void QCalendarWidget::showSelectedDate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget16showSelectedDateEv(QCalendarWidget *self) {
  self->showSelectedDate();
}

//  void QCalendarWidget::showToday()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCalendarWidget9showTodayEv(QCalendarWidget *self) {
  self->showToday();
}

//  a Python function taken by a CuteQCalendarWidget, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCalendarWidget(
    QCalendarWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCalendarWidget *>(self)->take(key, call);
}

//  QSize QCalendarWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QCalendarWidget8sizeHintEv(
    const QCalendarWidget *self) {
  return new QSize(self->QCalendarWidget::sizeHint());
}

//  QSize QCalendarWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QCalendarWidget15minimumSizeHintEv(
    const QCalendarWidget *self) {
  return new QSize(self->QCalendarWidget::minimumSizeHint());
}

//  bool QCalendarWidget::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QCalendarWidget5eventEP6QEvent(
    QCalendarWidget *self,
    QEvent *event) {
  return static_cast<OwnQCalendarWidget *>(self)->OwnQCalendarWidget::event(
      event);
}

//  bool QCalendarWidget::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QCalendarWidget11eventFilterEP7QObjectP6QEvent(
    QCalendarWidget *self,
    QObject *watched,
    QEvent *event) {
  return static_cast<OwnQCalendarWidget *>(self)->OwnQCalendarWidget::eventFilter(
      watched,
      event);
}

//  void QCalendarWidget::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QCalendarWidget15mousePressEventEP11QMouseEvent(
    QCalendarWidget *self,
    QMouseEvent *event) {
  static_cast<OwnQCalendarWidget *>(self)->OwnQCalendarWidget::mousePressEvent(
      event);
}

//  void QCalendarWidget::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QCalendarWidget11resizeEventEP12QResizeEvent(
    QCalendarWidget *self,
    QResizeEvent *event) {
  static_cast<OwnQCalendarWidget *>(self)->OwnQCalendarWidget::resizeEvent(
      event);
}

//  void QCalendarWidget::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QCalendarWidget13keyPressEventEP9QKeyEvent(
    QCalendarWidget *self,
    QKeyEvent *event) {
  static_cast<OwnQCalendarWidget *>(self)->OwnQCalendarWidget::keyPressEvent(
      event);
}

//  void QCalendarWidget::paintCell(QPainter *painter, const QRect &rect,
//      QDate date) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK15QCalendarWidget9paintCellEP8QPainterRK5QRect5QDate(
    const QCalendarWidget *self,
    QPainter *painter,
    const QRect *rect,
    const QDate *date) {
  static_cast<const OwnQCalendarWidget *>(self)->OwnQCalendarWidget::paintCell(
      painter,
      *rect,
      *date);
}
