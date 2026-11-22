//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qscrollarea.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qscrollarea.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QScrollArea may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQScrollArea : QScrollArea {
  using QScrollArea::event;
  using QScrollArea::eventFilter;
  using QScrollArea::resizeEvent;
  using QScrollArea::scrollContentsBy;
  using QScrollArea::viewportSizeHint;
};

//  A QScrollArea that Python can take functions over in. Every QScrollArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQScrollAreaCall0)(const void *, int *);
typedef bool (*CuteQScrollAreaCall1)(const void *, bool, int *);
typedef bool (*CuteQScrollAreaCall2)(const void *, QEvent *, int *);
typedef bool (*CuteQScrollAreaCall3)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQScrollAreaCall4)(const void *, QResizeEvent *, int *);
typedef void (*CuteQScrollAreaCall5)(const void *, int, int, int *);
typedef const QSize * (*CuteQScrollAreaCall6)(const void *, int *);
typedef const QSize * (*CuteQScrollAreaCall7)(const void *, int *);
typedef void (*CuteQScrollAreaCall8)(const void *, QWidget *, int *);
typedef bool (*CuteQScrollAreaCall9)(const void *, QEvent *, int *);
typedef void (*CuteQScrollAreaCall10)(const void *, QPaintEvent *, int *);
typedef void (*CuteQScrollAreaCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQScrollAreaCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQScrollAreaCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQScrollAreaCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQScrollAreaCall15)(const void *, QWheelEvent *, int *);
typedef void (*CuteQScrollAreaCall16)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQScrollAreaCall17)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQScrollAreaCall18)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQScrollAreaCall19)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQScrollAreaCall20)(const void *, QDropEvent *, int *);
typedef void (*CuteQScrollAreaCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQScrollAreaCall22)(const void *, QEvent *, int *);
typedef void (*CuteQScrollAreaCall23)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQScrollAreaCall24)(const void *, int *);
typedef void (*CuteQScrollAreaCall25)(const void *, bool, int *);
typedef int (*CuteQScrollAreaCall26)(const void *, int, int *);
typedef bool (*CuteQScrollAreaCall27)(const void *, int *);
typedef void * (*CuteQScrollAreaCall28)(const void *, int *);
typedef void (*CuteQScrollAreaCall29)(const void *, QKeyEvent *, int *);
typedef void (*CuteQScrollAreaCall30)(const void *, QFocusEvent *, int *);
typedef void (*CuteQScrollAreaCall31)(const void *, QFocusEvent *, int *);
typedef void (*CuteQScrollAreaCall32)(const void *, QEnterEvent *, int *);
typedef void (*CuteQScrollAreaCall33)(const void *, QEvent *, int *);
typedef void (*CuteQScrollAreaCall34)(const void *, QMoveEvent *, int *);
typedef void (*CuteQScrollAreaCall35)(const void *, QCloseEvent *, int *);
typedef void (*CuteQScrollAreaCall36)(const void *, QTabletEvent *, int *);
typedef void (*CuteQScrollAreaCall37)(const void *, QActionEvent *, int *);
typedef void (*CuteQScrollAreaCall38)(const void *, QShowEvent *, int *);
typedef void (*CuteQScrollAreaCall39)(const void *, QHideEvent *, int *);
typedef int (*CuteQScrollAreaCall40)(const void *, int, int *);
typedef void (*CuteQScrollAreaCall41)(const void *, QPainter *, int *);
typedef void * (*CuteQScrollAreaCall42)(const void *, QPoint *, int *);
typedef void * (*CuteQScrollAreaCall43)(const void *, int *);
typedef void (*CuteQScrollAreaCall44)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQScrollAreaCall45)(const void *, int, int *);
typedef void (*CuteQScrollAreaCall46)(const void *, QTimerEvent *, int *);
typedef void (*CuteQScrollAreaCall47)(const void *, QChildEvent *, int *);
typedef void (*CuteQScrollAreaCall48)(const void *, QEvent *, int *);
typedef void (*CuteQScrollAreaCall49)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQScrollAreaCall50)(const void *, const QMetaMethod *, int *);
class CuteQScrollArea : public QScrollArea {
public:
  using QScrollArea::QScrollArea;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
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
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
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

  //  QSize QScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScrollAreaCall0 call = reinterpret_cast<CuteQScrollAreaCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QScrollArea::sizeHint();
  }

  //  bool QScrollArea::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScrollAreaCall1 call = reinterpret_cast<CuteQScrollAreaCall1>(taken[1]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QScrollArea::focusNextPrevChild(next);
  }

  //  bool QScrollArea::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQScrollAreaCall2 call = reinterpret_cast<CuteQScrollAreaCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QScrollArea::event(a0);
  }

  //  bool QScrollArea::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScrollAreaCall3 call = reinterpret_cast<CuteQScrollAreaCall3>(taken[3]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QScrollArea::eventFilter(a0, a1);
  }

  //  void QScrollArea::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQScrollAreaCall4 call = reinterpret_cast<CuteQScrollAreaCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QScrollArea::resizeEvent(a0);
  }

  //  void QScrollArea::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[5]) {
      int handled = 0;
      CuteQScrollAreaCall5 call = reinterpret_cast<CuteQScrollAreaCall5>(taken[5]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QScrollArea::scrollContentsBy(dx, dy);
  }

  //  QSize QScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQScrollAreaCall6 call = reinterpret_cast<CuteQScrollAreaCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QScrollArea::viewportSizeHint();
  }

  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQScrollAreaCall7 call = reinterpret_cast<CuteQScrollAreaCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }

  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[8]) {
      int handled = 0;
      CuteQScrollAreaCall8 call = reinterpret_cast<CuteQScrollAreaCall8>(taken[8]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }

  //  bool QAbstractScrollArea::viewportEvent(QEvent *a0)
  bool viewportEvent(QEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQScrollAreaCall9 call = reinterpret_cast<CuteQScrollAreaCall9>(taken[9]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::viewportEvent(a0);
  }

  //  void QAbstractScrollArea::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQScrollAreaCall10 call = reinterpret_cast<CuteQScrollAreaCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::paintEvent(a0);
  }

  //  void QAbstractScrollArea::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQScrollAreaCall11 call = reinterpret_cast<CuteQScrollAreaCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mousePressEvent(a0);
  }

  //  void QAbstractScrollArea::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQScrollAreaCall12 call = reinterpret_cast<CuteQScrollAreaCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseReleaseEvent(a0);
  }

  //  void QAbstractScrollArea::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQScrollAreaCall13 call = reinterpret_cast<CuteQScrollAreaCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseDoubleClickEvent(a0);
  }

  //  void QAbstractScrollArea::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQScrollAreaCall14 call = reinterpret_cast<CuteQScrollAreaCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseMoveEvent(a0);
  }

  //  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQScrollAreaCall15 call = reinterpret_cast<CuteQScrollAreaCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::wheelEvent(a0);
  }

  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQScrollAreaCall16 call = reinterpret_cast<CuteQScrollAreaCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }

  //  void QAbstractScrollArea::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQScrollAreaCall17 call = reinterpret_cast<CuteQScrollAreaCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragEnterEvent(a0);
  }

  //  void QAbstractScrollArea::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQScrollAreaCall18 call = reinterpret_cast<CuteQScrollAreaCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragMoveEvent(a0);
  }

  //  void QAbstractScrollArea::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQScrollAreaCall19 call = reinterpret_cast<CuteQScrollAreaCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragLeaveEvent(a0);
  }

  //  void QAbstractScrollArea::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQScrollAreaCall20 call = reinterpret_cast<CuteQScrollAreaCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dropEvent(a0);
  }

  //  void QAbstractScrollArea::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQScrollAreaCall21 call = reinterpret_cast<CuteQScrollAreaCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::keyPressEvent(a0);
  }

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQScrollAreaCall22 call = reinterpret_cast<CuteQScrollAreaCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQScrollAreaCall23 call = reinterpret_cast<CuteQScrollAreaCall23>(taken[23]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQScrollAreaCall24 call = reinterpret_cast<CuteQScrollAreaCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[25]) {
      int handled = 0;
      CuteQScrollAreaCall25 call = reinterpret_cast<CuteQScrollAreaCall25>(taken[25]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQScrollAreaCall26 call = reinterpret_cast<CuteQScrollAreaCall26>(taken[26]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQScrollAreaCall27 call = reinterpret_cast<CuteQScrollAreaCall27>(taken[27]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQScrollAreaCall28 call = reinterpret_cast<CuteQScrollAreaCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQScrollAreaCall29 call = reinterpret_cast<CuteQScrollAreaCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQScrollAreaCall30 call = reinterpret_cast<CuteQScrollAreaCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQScrollAreaCall31 call = reinterpret_cast<CuteQScrollAreaCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQScrollAreaCall32 call = reinterpret_cast<CuteQScrollAreaCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQScrollAreaCall33 call = reinterpret_cast<CuteQScrollAreaCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQScrollAreaCall34 call = reinterpret_cast<CuteQScrollAreaCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQScrollAreaCall35 call = reinterpret_cast<CuteQScrollAreaCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQScrollAreaCall36 call = reinterpret_cast<CuteQScrollAreaCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQScrollAreaCall37 call = reinterpret_cast<CuteQScrollAreaCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQScrollAreaCall38 call = reinterpret_cast<CuteQScrollAreaCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQScrollAreaCall39 call = reinterpret_cast<CuteQScrollAreaCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQScrollAreaCall40 call = reinterpret_cast<CuteQScrollAreaCall40>(taken[40]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQScrollAreaCall41 call = reinterpret_cast<CuteQScrollAreaCall41>(taken[41]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQScrollAreaCall42 call = reinterpret_cast<CuteQScrollAreaCall42>(taken[42]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQScrollAreaCall43 call = reinterpret_cast<CuteQScrollAreaCall43>(taken[43]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQScrollAreaCall44 call = reinterpret_cast<CuteQScrollAreaCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQScrollAreaCall45 call = reinterpret_cast<CuteQScrollAreaCall45>(taken[45]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQScrollAreaCall46 call = reinterpret_cast<CuteQScrollAreaCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQScrollAreaCall47 call = reinterpret_cast<CuteQScrollAreaCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQScrollAreaCall48 call = reinterpret_cast<CuteQScrollAreaCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQScrollAreaCall49 call = reinterpret_cast<CuteQScrollAreaCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQScrollAreaCall50 call = reinterpret_cast<CuteQScrollAreaCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QScrollArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QScrollArea10metaObjectEv(
    const QScrollArea *self) {
  return self->metaObject();
}

//  QString QScrollArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QScrollArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScrollArea::tr(s, c, n));
}

//  QScrollArea::QScrollArea(QWidget *parent)
extern "C" Q_DECL_EXPORT
QScrollArea *ritual_ZN11QScrollAreaC1EP7QWidget(QWidget *parent) {
  return new CuteQScrollArea(parent);
}

//  QScrollArea::~QScrollArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollAreaD1Ev(QScrollArea *self) {
  delete self;
}

//  QWidget *QScrollArea::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QScrollArea6widgetEv(const QScrollArea *self) {
  return self->widget();
}

//  void QScrollArea::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea9setWidgetEP7QWidget(
    QScrollArea *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QScrollArea::takeWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN11QScrollArea10takeWidgetEv(QScrollArea *self) {
  return self->takeWidget();
}

//  bool QScrollArea::widgetResizable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QScrollArea15widgetResizableEv(const QScrollArea *self) {
  return self->widgetResizable();
}

//  void QScrollArea::setWidgetResizable(bool resizable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea18setWidgetResizableEb(
    QScrollArea *self,
    bool resizable) {
  self->setWidgetResizable(resizable);
}

//  QSize QScrollArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QScrollArea8sizeHintEv(const QScrollArea *self) {
  return new QSize(self->sizeHint());
}

//  bool QScrollArea::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QScrollArea18focusNextPrevChildEb(
    QScrollArea *self,
    bool next) {
  return self->focusNextPrevChild(next);
}

//  Qt::Alignment QScrollArea::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QScrollArea9alignmentEv(const QScrollArea *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QScrollArea::setAlignment(Qt::Alignment a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QScrollArea *self,
    int a0) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(a0));
}

//  void QScrollArea::ensureVisible(int x, int y, int xmargin, int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea13ensureVisibleEiiii(
    QScrollArea *self,
    int x,
    int y,
    int xmargin,
    int ymargin) {
  self->ensureVisible(x, y, xmargin, ymargin);
}

//  void QScrollArea::ensureWidgetVisible(QWidget *childWidget, int xmargin,
//      int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScrollArea19ensureWidgetVisibleEP7QWidgetii(
    QScrollArea *self,
    QWidget *childWidget,
    int xmargin,
    int ymargin) {
  self->ensureWidgetVisible(childWidget, xmargin, ymargin);
}

//  a Python function taken by a CuteQScrollArea, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScrollArea(
    QScrollArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScrollArea *>(self)->take(key, call);
}

//  QSize QScrollArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QScrollArea8sizeHintEv(const QScrollArea *self) {
  return new QSize(self->QScrollArea::sizeHint());
}

//  bool QScrollArea::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QScrollArea18focusNextPrevChildEb(
    QScrollArea *self,
    bool next) {
  return self->QScrollArea::focusNextPrevChild(next);
}

//  bool QScrollArea::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QScrollArea5eventEP6QEvent(
    QScrollArea *self,
    QEvent *a0) {
  return static_cast<OwnQScrollArea *>(self)->OwnQScrollArea::event(a0);
}

//  bool QScrollArea::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QScrollArea11eventFilterEP7QObjectP6QEvent(
    QScrollArea *self,
    QObject *a0,
    QEvent *a1) {
  return static_cast<OwnQScrollArea *>(self)->OwnQScrollArea::eventFilter(
      a0,
      a1);
}

//  void QScrollArea::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QScrollArea11resizeEventEP12QResizeEvent(
    QScrollArea *self,
    QResizeEvent *a0) {
  static_cast<OwnQScrollArea *>(self)->OwnQScrollArea::resizeEvent(a0);
}

//  void QScrollArea::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QScrollArea16scrollContentsByEii(
    QScrollArea *self,
    int dx,
    int dy) {
  static_cast<OwnQScrollArea *>(self)->OwnQScrollArea::scrollContentsBy(
      dx,
      dy);
}

//  QSize QScrollArea::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QScrollArea16viewportSizeHintEv(
    const QScrollArea *self) {
  return new QSize(
      static_cast<const OwnQScrollArea *>(self)->OwnQScrollArea::viewportSizeHint());
}
