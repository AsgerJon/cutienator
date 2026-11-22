//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmdiarea.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmdiarea.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtWidgets/qmdisubwindow.h>
#include <QtGui/qbrush.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QMdiArea may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMdiArea : QMdiArea {
  using QMdiArea::setupViewport;
  using QMdiArea::event;
  using QMdiArea::eventFilter;
  using QMdiArea::paintEvent;
  using QMdiArea::childEvent;
  using QMdiArea::resizeEvent;
  using QMdiArea::timerEvent;
  using QMdiArea::showEvent;
  using QMdiArea::viewportEvent;
  using QMdiArea::scrollContentsBy;
};

//  A QMdiArea that Python can take functions over in. Every QMdiArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQMdiAreaCall0)(const void *, int *);
typedef const QSize * (*CuteQMdiAreaCall1)(const void *, int *);
typedef void (*CuteQMdiAreaCall2)(const void *, QWidget *, int *);
typedef bool (*CuteQMdiAreaCall3)(const void *, QEvent *, int *);
typedef bool (*CuteQMdiAreaCall4)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQMdiAreaCall5)(const void *, QPaintEvent *, int *);
typedef void (*CuteQMdiAreaCall6)(const void *, QChildEvent *, int *);
typedef void (*CuteQMdiAreaCall7)(const void *, QResizeEvent *, int *);
typedef void (*CuteQMdiAreaCall8)(const void *, QTimerEvent *, int *);
typedef void (*CuteQMdiAreaCall9)(const void *, QShowEvent *, int *);
typedef bool (*CuteQMdiAreaCall10)(const void *, QEvent *, int *);
typedef void (*CuteQMdiAreaCall11)(const void *, int, int, int *);
typedef void (*CuteQMdiAreaCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMdiAreaCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMdiAreaCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMdiAreaCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMdiAreaCall16)(const void *, QWheelEvent *, int *);
typedef void (*CuteQMdiAreaCall17)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQMdiAreaCall18)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQMdiAreaCall19)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQMdiAreaCall20)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQMdiAreaCall21)(const void *, QDropEvent *, int *);
typedef void (*CuteQMdiAreaCall22)(const void *, QKeyEvent *, int *);
typedef const QSize * (*CuteQMdiAreaCall23)(const void *, int *);
typedef void (*CuteQMdiAreaCall24)(const void *, QEvent *, int *);
typedef void (*CuteQMdiAreaCall25)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQMdiAreaCall26)(const void *, int *);
typedef void (*CuteQMdiAreaCall27)(const void *, bool, int *);
typedef int (*CuteQMdiAreaCall28)(const void *, int, int *);
typedef bool (*CuteQMdiAreaCall29)(const void *, int *);
typedef void * (*CuteQMdiAreaCall30)(const void *, int *);
typedef void (*CuteQMdiAreaCall31)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMdiAreaCall32)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMdiAreaCall33)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMdiAreaCall34)(const void *, QEnterEvent *, int *);
typedef void (*CuteQMdiAreaCall35)(const void *, QEvent *, int *);
typedef void (*CuteQMdiAreaCall36)(const void *, QMoveEvent *, int *);
typedef void (*CuteQMdiAreaCall37)(const void *, QCloseEvent *, int *);
typedef void (*CuteQMdiAreaCall38)(const void *, QTabletEvent *, int *);
typedef void (*CuteQMdiAreaCall39)(const void *, QActionEvent *, int *);
typedef void (*CuteQMdiAreaCall40)(const void *, QHideEvent *, int *);
typedef int (*CuteQMdiAreaCall41)(const void *, int, int *);
typedef void (*CuteQMdiAreaCall42)(const void *, QPainter *, int *);
typedef void * (*CuteQMdiAreaCall43)(const void *, QPoint *, int *);
typedef void * (*CuteQMdiAreaCall44)(const void *, int *);
typedef void (*CuteQMdiAreaCall45)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQMdiAreaCall46)(const void *, int, int *);
typedef bool (*CuteQMdiAreaCall47)(const void *, bool, int *);
typedef void (*CuteQMdiAreaCall48)(const void *, QEvent *, int *);
typedef void (*CuteQMdiAreaCall49)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQMdiAreaCall50)(const void *, const QMetaMethod *, int *);
class CuteQMdiArea : public QMdiArea {
public:
  using QMdiArea::QMdiArea;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
    return false;
  }

  //  QSize QMdiArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMdiAreaCall0 call = reinterpret_cast<CuteQMdiAreaCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMdiArea::sizeHint();
  }

  //  QSize QMdiArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMdiAreaCall1 call = reinterpret_cast<CuteQMdiAreaCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMdiArea::minimumSizeHint();
  }

  //  void QMdiArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMdiAreaCall2 call = reinterpret_cast<CuteQMdiAreaCall2>(taken[2]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QMdiArea::setupViewport(viewport);
  }

  //  bool QMdiArea::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMdiAreaCall3 call = reinterpret_cast<CuteQMdiAreaCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QMdiArea::event(event);
  }

  //  bool QMdiArea::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMdiAreaCall4 call = reinterpret_cast<CuteQMdiAreaCall4>(taken[4]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QMdiArea::eventFilter(object, event);
  }

  //  void QMdiArea::paintEvent(QPaintEvent *paintEvent)
  void paintEvent(QPaintEvent *paintEvent) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMdiAreaCall5 call = reinterpret_cast<CuteQMdiAreaCall5>(taken[5]);
      call(this, paintEvent, &handled);
      if (handled) return;
    }
    QMdiArea::paintEvent(paintEvent);
  }

  //  void QMdiArea::childEvent(QChildEvent *childEvent)
  void childEvent(QChildEvent *childEvent) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMdiAreaCall6 call = reinterpret_cast<CuteQMdiAreaCall6>(taken[6]);
      call(this, childEvent, &handled);
      if (handled) return;
    }
    QMdiArea::childEvent(childEvent);
  }

  //  void QMdiArea::resizeEvent(QResizeEvent *resizeEvent)
  void resizeEvent(QResizeEvent *resizeEvent) override {
    if (taken[7]) {
      int handled = 0;
      CuteQMdiAreaCall7 call = reinterpret_cast<CuteQMdiAreaCall7>(taken[7]);
      call(this, resizeEvent, &handled);
      if (handled) return;
    }
    QMdiArea::resizeEvent(resizeEvent);
  }

  //  void QMdiArea::timerEvent(QTimerEvent *timerEvent)
  void timerEvent(QTimerEvent *timerEvent) override {
    if (taken[8]) {
      int handled = 0;
      CuteQMdiAreaCall8 call = reinterpret_cast<CuteQMdiAreaCall8>(taken[8]);
      call(this, timerEvent, &handled);
      if (handled) return;
    }
    QMdiArea::timerEvent(timerEvent);
  }

  //  void QMdiArea::showEvent(QShowEvent *showEvent)
  void showEvent(QShowEvent *showEvent) override {
    if (taken[9]) {
      int handled = 0;
      CuteQMdiAreaCall9 call = reinterpret_cast<CuteQMdiAreaCall9>(taken[9]);
      call(this, showEvent, &handled);
      if (handled) return;
    }
    QMdiArea::showEvent(showEvent);
  }

  //  bool QMdiArea::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQMdiAreaCall10 call = reinterpret_cast<CuteQMdiAreaCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QMdiArea::viewportEvent(event);
  }

  //  void QMdiArea::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[11]) {
      int handled = 0;
      CuteQMdiAreaCall11 call = reinterpret_cast<CuteQMdiAreaCall11>(taken[11]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QMdiArea::scrollContentsBy(dx, dy);
  }

  //  void QAbstractScrollArea::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQMdiAreaCall12 call = reinterpret_cast<CuteQMdiAreaCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mousePressEvent(a0);
  }

  //  void QAbstractScrollArea::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQMdiAreaCall13 call = reinterpret_cast<CuteQMdiAreaCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseReleaseEvent(a0);
  }

  //  void QAbstractScrollArea::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQMdiAreaCall14 call = reinterpret_cast<CuteQMdiAreaCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseDoubleClickEvent(a0);
  }

  //  void QAbstractScrollArea::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQMdiAreaCall15 call = reinterpret_cast<CuteQMdiAreaCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseMoveEvent(a0);
  }

  //  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQMdiAreaCall16 call = reinterpret_cast<CuteQMdiAreaCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::wheelEvent(a0);
  }

  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQMdiAreaCall17 call = reinterpret_cast<CuteQMdiAreaCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }

  //  void QAbstractScrollArea::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQMdiAreaCall18 call = reinterpret_cast<CuteQMdiAreaCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragEnterEvent(a0);
  }

  //  void QAbstractScrollArea::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQMdiAreaCall19 call = reinterpret_cast<CuteQMdiAreaCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragMoveEvent(a0);
  }

  //  void QAbstractScrollArea::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQMdiAreaCall20 call = reinterpret_cast<CuteQMdiAreaCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragLeaveEvent(a0);
  }

  //  void QAbstractScrollArea::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQMdiAreaCall21 call = reinterpret_cast<CuteQMdiAreaCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dropEvent(a0);
  }

  //  void QAbstractScrollArea::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQMdiAreaCall22 call = reinterpret_cast<CuteQMdiAreaCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::keyPressEvent(a0);
  }

  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQMdiAreaCall23 call = reinterpret_cast<CuteQMdiAreaCall23>(taken[23]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::viewportSizeHint();
  }

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQMdiAreaCall24 call = reinterpret_cast<CuteQMdiAreaCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQMdiAreaCall25 call = reinterpret_cast<CuteQMdiAreaCall25>(taken[25]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQMdiAreaCall26 call = reinterpret_cast<CuteQMdiAreaCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[27]) {
      int handled = 0;
      CuteQMdiAreaCall27 call = reinterpret_cast<CuteQMdiAreaCall27>(taken[27]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQMdiAreaCall28 call = reinterpret_cast<CuteQMdiAreaCall28>(taken[28]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQMdiAreaCall29 call = reinterpret_cast<CuteQMdiAreaCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQMdiAreaCall30 call = reinterpret_cast<CuteQMdiAreaCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQMdiAreaCall31 call = reinterpret_cast<CuteQMdiAreaCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQMdiAreaCall32 call = reinterpret_cast<CuteQMdiAreaCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQMdiAreaCall33 call = reinterpret_cast<CuteQMdiAreaCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQMdiAreaCall34 call = reinterpret_cast<CuteQMdiAreaCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQMdiAreaCall35 call = reinterpret_cast<CuteQMdiAreaCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQMdiAreaCall36 call = reinterpret_cast<CuteQMdiAreaCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQMdiAreaCall37 call = reinterpret_cast<CuteQMdiAreaCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQMdiAreaCall38 call = reinterpret_cast<CuteQMdiAreaCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQMdiAreaCall39 call = reinterpret_cast<CuteQMdiAreaCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQMdiAreaCall40 call = reinterpret_cast<CuteQMdiAreaCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQMdiAreaCall41 call = reinterpret_cast<CuteQMdiAreaCall41>(taken[41]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQMdiAreaCall42 call = reinterpret_cast<CuteQMdiAreaCall42>(taken[42]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQMdiAreaCall43 call = reinterpret_cast<CuteQMdiAreaCall43>(taken[43]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQMdiAreaCall44 call = reinterpret_cast<CuteQMdiAreaCall44>(taken[44]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQMdiAreaCall45 call = reinterpret_cast<CuteQMdiAreaCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQMdiAreaCall46 call = reinterpret_cast<CuteQMdiAreaCall46>(taken[46]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[47]) {
      int handled = 0;
      CuteQMdiAreaCall47 call = reinterpret_cast<CuteQMdiAreaCall47>(taken[47]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQMdiAreaCall48 call = reinterpret_cast<CuteQMdiAreaCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQMdiAreaCall49 call = reinterpret_cast<CuteQMdiAreaCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQMdiAreaCall50 call = reinterpret_cast<CuteQMdiAreaCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QMdiArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QMdiArea10metaObjectEv(const QMdiArea *self) {
  return self->metaObject();
}

//  QString QMdiArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QMdiArea2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QMdiArea::tr(s, c, n));
}

//  QMdiArea::QMdiArea(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMdiArea *ritual_ZN8QMdiAreaC1EP7QWidget(QWidget *parent) {
  return new CuteQMdiArea(parent);
}

//  QMdiArea::~QMdiArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiAreaD1Ev(QMdiArea *self) {
  delete self;
}

//  QSize QMdiArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QMdiArea8sizeHintEv(const QMdiArea *self) {
  return new QSize(self->sizeHint());
}

//  QSize QMdiArea::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QMdiArea15minimumSizeHintEv(const QMdiArea *self) {
  return new QSize(self->minimumSizeHint());
}

//  QMdiSubWindow *QMdiArea::currentSubWindow() const
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZNK8QMdiArea16currentSubWindowEv(
    const QMdiArea *self) {
  return self->currentSubWindow();
}

//  QMdiSubWindow *QMdiArea::activeSubWindow() const
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZNK8QMdiArea15activeSubWindowEv(const QMdiArea *self) {
  return self->activeSubWindow();
}

//  QList<QMdiSubWindow *> QMdiArea::subWindowList(WindowOrder order) const
extern "C" Q_DECL_EXPORT
QList<QMdiSubWindow *> *ritual_ZNK8QMdiArea13subWindowListENS_11WindowOrderE(
    const QMdiArea *self,
    QMdiArea::WindowOrder order) {
  return new QList<QMdiSubWindow *>(self->subWindowList(order));
}

//  QMdiSubWindow *QMdiArea::addSubWindow(QWidget *widget, Qt::WindowFlags
//      flags)
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZN8QMdiArea12addSubWindowEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QMdiArea *self,
    QWidget *widget,
    int flags) {
  return self->addSubWindow(widget, QFlags<Qt::WindowType>::fromInt(flags));
}

//  void QMdiArea::removeSubWindow(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea15removeSubWindowEP7QWidget(
    QMdiArea *self,
    QWidget *widget) {
  self->removeSubWindow(widget);
}

//  QBrush QMdiArea::background() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QMdiArea10backgroundEv(const QMdiArea *self) {
  return new QBrush(self->background());
}

//  void QMdiArea::setBackground(const QBrush &background)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea13setBackgroundERK6QBrush(
    QMdiArea *self,
    const QBrush *background) {
  self->setBackground(*background);
}

//  WindowOrder QMdiArea::activationOrder() const
extern "C" Q_DECL_EXPORT
QMdiArea::WindowOrder ritual_ZNK8QMdiArea15activationOrderEv(
    const QMdiArea *self) {
  return self->activationOrder();
}

//  void QMdiArea::setActivationOrder(WindowOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea18setActivationOrderENS_11WindowOrderE(
    QMdiArea *self,
    QMdiArea::WindowOrder order) {
  self->setActivationOrder(order);
}

//  void QMdiArea::setOption(AreaOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea9setOptionENS_10AreaOptionEb(
    QMdiArea *self,
    QMdiArea::AreaOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QMdiArea::testOption(AreaOption opton) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMdiArea10testOptionENS_10AreaOptionE(
    const QMdiArea *self,
    QMdiArea::AreaOption opton) {
  return self->testOption(opton);
}

//  void QMdiArea::setViewMode(ViewMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea11setViewModeENS_8ViewModeE(
    QMdiArea *self,
    QMdiArea::ViewMode mode) {
  self->setViewMode(mode);
}

//  ViewMode QMdiArea::viewMode() const
extern "C" Q_DECL_EXPORT
QMdiArea::ViewMode ritual_ZNK8QMdiArea8viewModeEv(const QMdiArea *self) {
  return self->viewMode();
}

//  bool QMdiArea::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMdiArea12documentModeEv(const QMdiArea *self) {
  return self->documentMode();
}

//  void QMdiArea::setDocumentMode(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea15setDocumentModeEb(QMdiArea *self, bool enabled) {
  self->setDocumentMode(enabled);
}

//  void QMdiArea::setTabsClosable(bool closable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea15setTabsClosableEb(QMdiArea *self, bool closable) {
  self->setTabsClosable(closable);
}

//  bool QMdiArea::tabsClosable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMdiArea12tabsClosableEv(const QMdiArea *self) {
  return self->tabsClosable();
}

//  void QMdiArea::setTabsMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea14setTabsMovableEb(QMdiArea *self, bool movable) {
  self->setTabsMovable(movable);
}

//  bool QMdiArea::tabsMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMdiArea11tabsMovableEv(const QMdiArea *self) {
  return self->tabsMovable();
}

//  void QMdiArea::setTabShape(QTabWidget::TabShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea11setTabShapeEN10QTabWidget8TabShapeE(
    QMdiArea *self,
    QTabWidget::TabShape shape) {
  self->setTabShape(shape);
}

//  QTabWidget::TabShape QMdiArea::tabShape() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabShape ritual_ZNK8QMdiArea8tabShapeEv(const QMdiArea *self) {
  return self->tabShape();
}

//  void QMdiArea::setTabPosition(QTabWidget::TabPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea14setTabPositionEN10QTabWidget11TabPositionE(
    QMdiArea *self,
    QTabWidget::TabPosition position) {
  self->setTabPosition(position);
}

//  QTabWidget::TabPosition QMdiArea::tabPosition() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabPosition ritual_ZNK8QMdiArea11tabPositionEv(
    const QMdiArea *self) {
  return self->tabPosition();
}

//  void QMdiArea::setActiveSubWindow(QMdiSubWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea18setActiveSubWindowEP13QMdiSubWindow(
    QMdiArea *self,
    QMdiSubWindow *window) {
  self->setActiveSubWindow(window);
}

//  void QMdiArea::tileSubWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea14tileSubWindowsEv(QMdiArea *self) {
  self->tileSubWindows();
}

//  void QMdiArea::cascadeSubWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea17cascadeSubWindowsEv(QMdiArea *self) {
  self->cascadeSubWindows();
}

//  void QMdiArea::closeActiveSubWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea20closeActiveSubWindowEv(QMdiArea *self) {
  self->closeActiveSubWindow();
}

//  void QMdiArea::closeAllSubWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea18closeAllSubWindowsEv(QMdiArea *self) {
  self->closeAllSubWindows();
}

//  void QMdiArea::activateNextSubWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea21activateNextSubWindowEv(QMdiArea *self) {
  self->activateNextSubWindow();
}

//  void QMdiArea::activatePreviousSubWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea25activatePreviousSubWindowEv(QMdiArea *self) {
  self->activatePreviousSubWindow();
}

//  a Python function taken by a CuteQMdiArea, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMdiArea(QMdiArea *self, const char *key, void *call) {
  return static_cast<CuteQMdiArea *>(self)->take(key, call);
}

//  QSize QMdiArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK8QMdiArea8sizeHintEv(const QMdiArea *self) {
  return new QSize(self->QMdiArea::sizeHint());
}

//  QSize QMdiArea::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK8QMdiArea15minimumSizeHintEv(const QMdiArea *self) {
  return new QSize(self->QMdiArea::minimumSizeHint());
}

//  void QMdiArea::setupViewport(QWidget *viewport)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMdiArea13setupViewportEP7QWidget(
    QMdiArea *self,
    QWidget *viewport) {
  static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::setupViewport(viewport);
}

//  bool QMdiArea::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QMdiArea5eventEP6QEvent(QMdiArea *self, QEvent *event) {
  return static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::event(event);
}

//  bool QMdiArea::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QMdiArea11eventFilterEP7QObjectP6QEvent(
    QMdiArea *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::eventFilter(
      object,
      event);
}

//  void QMdiArea::paintEvent(QPaintEvent *paintEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMdiArea10paintEventEP11QPaintEvent(
    QMdiArea *self,
    QPaintEvent *paintEvent) {
  static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::paintEvent(paintEvent);
}

//  void QMdiArea::childEvent(QChildEvent *childEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMdiArea10childEventEP11QChildEvent(
    QMdiArea *self,
    QChildEvent *childEvent) {
  static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::childEvent(childEvent);
}

//  void QMdiArea::resizeEvent(QResizeEvent *resizeEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMdiArea11resizeEventEP12QResizeEvent(
    QMdiArea *self,
    QResizeEvent *resizeEvent) {
  static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::resizeEvent(resizeEvent);
}

//  void QMdiArea::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMdiArea10timerEventEP11QTimerEvent(
    QMdiArea *self,
    QTimerEvent *timerEvent) {
  static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::timerEvent(timerEvent);
}

//  void QMdiArea::showEvent(QShowEvent *showEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMdiArea9showEventEP10QShowEvent(
    QMdiArea *self,
    QShowEvent *showEvent) {
  static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::showEvent(showEvent);
}

//  bool QMdiArea::viewportEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QMdiArea13viewportEventEP6QEvent(
    QMdiArea *self,
    QEvent *event) {
  return static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::viewportEvent(event);
}

//  void QMdiArea::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QMdiArea16scrollContentsByEii(
    QMdiArea *self,
    int dx,
    int dy) {
  static_cast<OwnQMdiArea *>(self)->OwnQMdiArea::scrollContentsBy(dx, dy);
}
