//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractscrollarea.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/qabstractscrollarea.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QAbstractScrollArea may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractScrollArea : QAbstractScrollArea {
  using QAbstractScrollArea::eventFilter;
  using QAbstractScrollArea::event;
  using QAbstractScrollArea::viewportEvent;
  using QAbstractScrollArea::resizeEvent;
  using QAbstractScrollArea::paintEvent;
  using QAbstractScrollArea::mousePressEvent;
  using QAbstractScrollArea::mouseReleaseEvent;
  using QAbstractScrollArea::mouseDoubleClickEvent;
  using QAbstractScrollArea::mouseMoveEvent;
  using QAbstractScrollArea::wheelEvent;
  using QAbstractScrollArea::contextMenuEvent;
  using QAbstractScrollArea::dragEnterEvent;
  using QAbstractScrollArea::dragMoveEvent;
  using QAbstractScrollArea::dragLeaveEvent;
  using QAbstractScrollArea::dropEvent;
  using QAbstractScrollArea::keyPressEvent;
  using QAbstractScrollArea::scrollContentsBy;
  using QAbstractScrollArea::viewportSizeHint;
};

//  A QAbstractScrollArea that Python can take functions over in. Every QAbstractScrollArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQAbstractScrollAreaCall0)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQAbstractScrollAreaCall1)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall2)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQAbstractScrollAreaCall3)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQAbstractScrollAreaCall4)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQAbstractScrollAreaCall5)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall6)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall7)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall8)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall9)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall10)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall11)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall12)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall14)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall15)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall16)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall17)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall18)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall19)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQAbstractScrollAreaCall20)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaCall21)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractScrollAreaCall22)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQAbstractScrollAreaCall23)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaCall24)(const void *, bool, int *);
typedef int (*CuteQAbstractScrollAreaCall25)(const void *, int, int *);
typedef bool (*CuteQAbstractScrollAreaCall26)(const void *, int *);
typedef void * (*CuteQAbstractScrollAreaCall27)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaCall28)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstractScrollAreaCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstractScrollAreaCall30)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAbstractScrollAreaCall31)(const void *, QEnterEvent *, int *);
typedef void (*CuteQAbstractScrollAreaCall32)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractScrollAreaCall33)(const void *, QMoveEvent *, int *);
typedef void (*CuteQAbstractScrollAreaCall34)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQAbstractScrollAreaCall35)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQAbstractScrollAreaCall36)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQAbstractScrollAreaCall37)(const void *, QShowEvent *, int *);
typedef void (*CuteQAbstractScrollAreaCall38)(const void *, QHideEvent *, int *);
typedef int (*CuteQAbstractScrollAreaCall39)(const void *, int, int *);
typedef void (*CuteQAbstractScrollAreaCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQAbstractScrollAreaCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQAbstractScrollAreaCall42)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQAbstractScrollAreaCall44)(const void *, int, int *);
typedef bool (*CuteQAbstractScrollAreaCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractScrollAreaCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractScrollAreaCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractScrollAreaCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractScrollAreaCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractScrollAreaCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractScrollArea : public QAbstractScrollArea {
public:
  using QAbstractScrollArea::QAbstractScrollArea;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[34] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[45] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall0 call = reinterpret_cast<CuteQAbstractScrollAreaCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall1 call = reinterpret_cast<CuteQAbstractScrollAreaCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall2 call = reinterpret_cast<CuteQAbstractScrollAreaCall2>(taken[2]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall3 call = reinterpret_cast<CuteQAbstractScrollAreaCall3>(taken[3]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollArea::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall4 call = reinterpret_cast<CuteQAbstractScrollAreaCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::event(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollArea::viewportEvent(QEvent *a0)
  bool viewportEvent(QEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall5 call = reinterpret_cast<CuteQAbstractScrollAreaCall5>(taken[5]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::viewportEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall6 call = reinterpret_cast<CuteQAbstractScrollAreaCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::resizeEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall7 call = reinterpret_cast<CuteQAbstractScrollAreaCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::paintEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall8 call = reinterpret_cast<CuteQAbstractScrollAreaCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall9 call = reinterpret_cast<CuteQAbstractScrollAreaCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall10 call = reinterpret_cast<CuteQAbstractScrollAreaCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseDoubleClickEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall11 call = reinterpret_cast<CuteQAbstractScrollAreaCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall12 call = reinterpret_cast<CuteQAbstractScrollAreaCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::wheelEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall13 call = reinterpret_cast<CuteQAbstractScrollAreaCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall14 call = reinterpret_cast<CuteQAbstractScrollAreaCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall15 call = reinterpret_cast<CuteQAbstractScrollAreaCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall16 call = reinterpret_cast<CuteQAbstractScrollAreaCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall17 call = reinterpret_cast<CuteQAbstractScrollAreaCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::dropEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall18 call = reinterpret_cast<CuteQAbstractScrollAreaCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall19 call = reinterpret_cast<CuteQAbstractScrollAreaCall19>(taken[19]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall20 call = reinterpret_cast<CuteQAbstractScrollAreaCall20>(taken[20]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::viewportSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall21 call = reinterpret_cast<CuteQAbstractScrollAreaCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall22 call = reinterpret_cast<CuteQAbstractScrollAreaCall22>(taken[22]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall23 call = reinterpret_cast<CuteQAbstractScrollAreaCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall24 call = reinterpret_cast<CuteQAbstractScrollAreaCall24>(taken[24]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall25 call = reinterpret_cast<CuteQAbstractScrollAreaCall25>(taken[25]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall26 call = reinterpret_cast<CuteQAbstractScrollAreaCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall27 call = reinterpret_cast<CuteQAbstractScrollAreaCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall28 call = reinterpret_cast<CuteQAbstractScrollAreaCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall29 call = reinterpret_cast<CuteQAbstractScrollAreaCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall30 call = reinterpret_cast<CuteQAbstractScrollAreaCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall31 call = reinterpret_cast<CuteQAbstractScrollAreaCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall32 call = reinterpret_cast<CuteQAbstractScrollAreaCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall33 call = reinterpret_cast<CuteQAbstractScrollAreaCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall34 call = reinterpret_cast<CuteQAbstractScrollAreaCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall35 call = reinterpret_cast<CuteQAbstractScrollAreaCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall36 call = reinterpret_cast<CuteQAbstractScrollAreaCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall37 call = reinterpret_cast<CuteQAbstractScrollAreaCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall38 call = reinterpret_cast<CuteQAbstractScrollAreaCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall39 call = reinterpret_cast<CuteQAbstractScrollAreaCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall40 call = reinterpret_cast<CuteQAbstractScrollAreaCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall41 call = reinterpret_cast<CuteQAbstractScrollAreaCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall42 call = reinterpret_cast<CuteQAbstractScrollAreaCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall43 call = reinterpret_cast<CuteQAbstractScrollAreaCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall44 call = reinterpret_cast<CuteQAbstractScrollAreaCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall45 call = reinterpret_cast<CuteQAbstractScrollAreaCall45>(taken[45]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall46 call = reinterpret_cast<CuteQAbstractScrollAreaCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall47 call = reinterpret_cast<CuteQAbstractScrollAreaCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall48 call = reinterpret_cast<CuteQAbstractScrollAreaCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall49 call = reinterpret_cast<CuteQAbstractScrollAreaCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQAbstractScrollAreaCall50 call = reinterpret_cast<CuteQAbstractScrollAreaCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractScrollArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractScrollArea10metaObjectEv(
    const QAbstractScrollArea *self) {
  return self->metaObject();
}

//  QString QAbstractScrollArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractScrollArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractScrollArea::tr(s, c, n));
}

//  QAbstractScrollArea::QAbstractScrollArea(QWidget *parent)
extern "C" Q_DECL_EXPORT
QAbstractScrollArea *ritual_ZN19QAbstractScrollAreaC1EP7QWidget(
    QWidget *parent) {
  return new CuteQAbstractScrollArea(parent);
}

//  QAbstractScrollArea::~QAbstractScrollArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollAreaD1Ev(QAbstractScrollArea *self) {
  delete self;
}

//  Qt::ScrollBarPolicy QAbstractScrollArea::verticalScrollBarPolicy() const
extern "C" Q_DECL_EXPORT
Qt::ScrollBarPolicy ritual_ZNK19QAbstractScrollArea23verticalScrollBarPolicyEv(
    const QAbstractScrollArea *self) {
  return self->verticalScrollBarPolicy();
}

//  void QAbstractScrollArea::setVerticalScrollBarPolicy(Qt::ScrollBarPolicy
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea26setVerticalScrollBarPolicyEN2Qt15ScrollBarPolicyE(
    QAbstractScrollArea *self,
    Qt::ScrollBarPolicy a0) {
  self->setVerticalScrollBarPolicy(a0);
}

//  QScrollBar *QAbstractScrollArea::verticalScrollBar() const
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZNK19QAbstractScrollArea17verticalScrollBarEv(
    const QAbstractScrollArea *self) {
  return self->verticalScrollBar();
}

//  void QAbstractScrollArea::setVerticalScrollBar(QScrollBar *scrollbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea20setVerticalScrollBarEP10QScrollBar(
    QAbstractScrollArea *self,
    QScrollBar *scrollbar) {
  self->setVerticalScrollBar(scrollbar);
}

//  Qt::ScrollBarPolicy QAbstractScrollArea::horizontalScrollBarPolicy()
//      const
extern "C" Q_DECL_EXPORT
Qt::ScrollBarPolicy ritual_ZNK19QAbstractScrollArea25horizontalScrollBarPolicyEv(
    const QAbstractScrollArea *self) {
  return self->horizontalScrollBarPolicy();
}

//  void
//      QAbstractScrollArea::setHorizontalScrollBarPolicy(Qt::ScrollBarPolicy
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea28setHorizontalScrollBarPolicyEN2Qt15ScrollBarPolicyE(
    QAbstractScrollArea *self,
    Qt::ScrollBarPolicy a0) {
  self->setHorizontalScrollBarPolicy(a0);
}

//  QScrollBar *QAbstractScrollArea::horizontalScrollBar() const
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZNK19QAbstractScrollArea19horizontalScrollBarEv(
    const QAbstractScrollArea *self) {
  return self->horizontalScrollBar();
}

//  void QAbstractScrollArea::setHorizontalScrollBar(QScrollBar *scrollbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea22setHorizontalScrollBarEP10QScrollBar(
    QAbstractScrollArea *self,
    QScrollBar *scrollbar) {
  self->setHorizontalScrollBar(scrollbar);
}

//  QWidget *QAbstractScrollArea::cornerWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QAbstractScrollArea12cornerWidgetEv(
    const QAbstractScrollArea *self) {
  return self->cornerWidget();
}

//  void QAbstractScrollArea::setCornerWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea15setCornerWidgetEP7QWidget(
    QAbstractScrollArea *self,
    QWidget *widget) {
  self->setCornerWidget(widget);
}

//  void QAbstractScrollArea::addScrollBarWidget(QWidget *widget,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea18addScrollBarWidgetEP7QWidget6QFlagsIN2Qt13AlignmentFlagEE(
    QAbstractScrollArea *self,
    QWidget *widget,
    int alignment) {
  self->addScrollBarWidget(
      widget,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QWidgetList QAbstractScrollArea::scrollBarWidgets(Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZN19QAbstractScrollArea16scrollBarWidgetsE6QFlagsIN2Qt13AlignmentFlagEE(
    QAbstractScrollArea *self,
    int alignment) {
  return new QList<QWidget *>(
      self->scrollBarWidgets(
          QFlags<Qt::AlignmentFlag>::fromInt(alignment)));
}

//  QWidget *QAbstractScrollArea::viewport() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QAbstractScrollArea8viewportEv(
    const QAbstractScrollArea *self) {
  return self->viewport();
}

//  void QAbstractScrollArea::setViewport(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea11setViewportEP7QWidget(
    QAbstractScrollArea *self,
    QWidget *widget) {
  self->setViewport(widget);
}

//  QSize QAbstractScrollArea::maximumViewportSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractScrollArea19maximumViewportSizeEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->maximumViewportSize());
}

//  QSize QAbstractScrollArea::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractScrollArea15minimumSizeHintEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->minimumSizeHint());
}

//  QSize QAbstractScrollArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractScrollArea8sizeHintEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->sizeHint());
}

//  void QAbstractScrollArea::setupViewport(QWidget *viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea13setupViewportEP7QWidget(
    QAbstractScrollArea *self,
    QWidget *viewport) {
  self->setupViewport(viewport);
}

//  SizeAdjustPolicy QAbstractScrollArea::sizeAdjustPolicy() const
extern "C" Q_DECL_EXPORT
QAbstractScrollArea::SizeAdjustPolicy ritual_ZNK19QAbstractScrollArea16sizeAdjustPolicyEv(
    const QAbstractScrollArea *self) {
  return self->sizeAdjustPolicy();
}

//  void QAbstractScrollArea::setSizeAdjustPolicy(SizeAdjustPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea19setSizeAdjustPolicyENS_16SizeAdjustPolicyE(
    QAbstractScrollArea *self,
    QAbstractScrollArea::SizeAdjustPolicy policy) {
  self->setSizeAdjustPolicy(policy);
}

//  void QAbstractScrollArea::setViewportMargins(int left, int top, int
//      right, int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea18setViewportMarginsEiiii(
    QAbstractScrollArea *self,
    int left,
    int top,
    int right,
    int bottom) {
  self->setViewportMargins(left, top, right, bottom);
}

//  void QAbstractScrollArea::setViewportMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea18setViewportMarginsERK8QMargins(
    QAbstractScrollArea *self,
    const QMargins *margins) {
  self->setViewportMargins(*margins);
}

//  QMargins QAbstractScrollArea::viewportMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK19QAbstractScrollArea15viewportMarginsEv(
    const QAbstractScrollArea *self) {
  return new QMargins(self->viewportMargins());
}

//  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractScrollArea11eventFilterEP7QObjectP6QEvent(
    QAbstractScrollArea *self,
    QObject *a0,
    QEvent *a1) {
  return self->eventFilter(a0, a1);
}

//  bool QAbstractScrollArea::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractScrollArea5eventEP6QEvent(
    QAbstractScrollArea *self,
    QEvent *a0) {
  return self->event(a0);
}

//  bool QAbstractScrollArea::viewportEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractScrollArea13viewportEventEP6QEvent(
    QAbstractScrollArea *self,
    QEvent *a0) {
  return self->viewportEvent(a0);
}

//  void QAbstractScrollArea::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea11resizeEventEP12QResizeEvent(
    QAbstractScrollArea *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QAbstractScrollArea::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea10paintEventEP11QPaintEvent(
    QAbstractScrollArea *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QAbstractScrollArea::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea15mousePressEventEP11QMouseEvent(
    QAbstractScrollArea *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QAbstractScrollArea::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea17mouseReleaseEventEP11QMouseEvent(
    QAbstractScrollArea *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QAbstractScrollArea::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea21mouseDoubleClickEventEP11QMouseEvent(
    QAbstractScrollArea *self,
    QMouseEvent *a0) {
  self->mouseDoubleClickEvent(a0);
}

//  void QAbstractScrollArea::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea14mouseMoveEventEP11QMouseEvent(
    QAbstractScrollArea *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

#if QT_CONFIG(wheelevent)
//  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea10wheelEventEP11QWheelEvent(
    QAbstractScrollArea *self,
    QWheelEvent *a0) {
  self->wheelEvent(a0);
}
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_CONTEXTMENU)
//  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea16contextMenuEventEP17QContextMenuEvent(
    QAbstractScrollArea *self,
    QContextMenuEvent *a0) {
  self->contextMenuEvent(a0);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
//  void QAbstractScrollArea::dragEnterEvent(QDragEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea14dragEnterEventEP15QDragEnterEvent(
    QAbstractScrollArea *self,
    QDragEnterEvent *a0) {
  self->dragEnterEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractScrollArea::dragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea13dragMoveEventEP14QDragMoveEvent(
    QAbstractScrollArea *self,
    QDragMoveEvent *a0) {
  self->dragMoveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractScrollArea::dragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea14dragLeaveEventEP15QDragLeaveEvent(
    QAbstractScrollArea *self,
    QDragLeaveEvent *a0) {
  self->dragLeaveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractScrollArea::dropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea9dropEventEP10QDropEvent(
    QAbstractScrollArea *self,
    QDropEvent *a0) {
  self->dropEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

//  void QAbstractScrollArea::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea13keyPressEventEP9QKeyEvent(
    QAbstractScrollArea *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QAbstractScrollArea::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractScrollArea16scrollContentsByEii(
    QAbstractScrollArea *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  QSize QAbstractScrollArea::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractScrollArea16viewportSizeHintEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->viewportSizeHint());
}

//  QAbstractScrollAreaPrivate *QAbstractScrollArea::d_func()
extern "C" Q_DECL_EXPORT
QAbstractScrollAreaPrivate *ritual_ZN19QAbstractScrollArea6d_funcEv(
    QAbstractScrollArea *self) {
  return self->d_func();
}

//  const QAbstractScrollAreaPrivate *QAbstractScrollArea::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractScrollAreaPrivate *ritual_ZNK19QAbstractScrollArea6d_funcEv(
    const QAbstractScrollArea *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractScrollArea, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractScrollArea(
    QAbstractScrollArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractScrollArea *>(self)->take(key, call);
}

//  QSize QAbstractScrollArea::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QAbstractScrollArea15minimumSizeHintEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->QAbstractScrollArea::minimumSizeHint());
}

//  QSize QAbstractScrollArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QAbstractScrollArea8sizeHintEv(
    const QAbstractScrollArea *self) {
  return new QSize(self->QAbstractScrollArea::sizeHint());
}

//  void QAbstractScrollArea::setupViewport(QWidget *viewport)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea13setupViewportEP7QWidget(
    QAbstractScrollArea *self,
    QWidget *viewport) {
  self->QAbstractScrollArea::setupViewport(viewport);
}

//  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractScrollArea11eventFilterEP7QObjectP6QEvent(
    QAbstractScrollArea *self,
    QObject *a0,
    QEvent *a1) {
  return static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::eventFilter(
      a0,
      a1);
}

//  bool QAbstractScrollArea::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractScrollArea5eventEP6QEvent(
    QAbstractScrollArea *self,
    QEvent *a0) {
  return static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::event(
      a0);
}

//  bool QAbstractScrollArea::viewportEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractScrollArea13viewportEventEP6QEvent(
    QAbstractScrollArea *self,
    QEvent *a0) {
  return static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::viewportEvent(
      a0);
}

//  void QAbstractScrollArea::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea11resizeEventEP12QResizeEvent(
    QAbstractScrollArea *self,
    QResizeEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::resizeEvent(
      a0);
}

//  void QAbstractScrollArea::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea10paintEventEP11QPaintEvent(
    QAbstractScrollArea *self,
    QPaintEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::paintEvent(
      a0);
}

//  void QAbstractScrollArea::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea15mousePressEventEP11QMouseEvent(
    QAbstractScrollArea *self,
    QMouseEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::mousePressEvent(
      a0);
}

//  void QAbstractScrollArea::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea17mouseReleaseEventEP11QMouseEvent(
    QAbstractScrollArea *self,
    QMouseEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::mouseReleaseEvent(
      a0);
}

//  void QAbstractScrollArea::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea21mouseDoubleClickEventEP11QMouseEvent(
    QAbstractScrollArea *self,
    QMouseEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::mouseDoubleClickEvent(
      a0);
}

//  void QAbstractScrollArea::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea14mouseMoveEventEP11QMouseEvent(
    QAbstractScrollArea *self,
    QMouseEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::mouseMoveEvent(
      a0);
}

#if QT_CONFIG(wheelevent)
//  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea10wheelEventEP11QWheelEvent(
    QAbstractScrollArea *self,
    QWheelEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::wheelEvent(
      a0);
}
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_CONTEXTMENU)
//  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea16contextMenuEventEP17QContextMenuEvent(
    QAbstractScrollArea *self,
    QContextMenuEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::contextMenuEvent(
      a0);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
//  void QAbstractScrollArea::dragEnterEvent(QDragEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea14dragEnterEventEP15QDragEnterEvent(
    QAbstractScrollArea *self,
    QDragEnterEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::dragEnterEvent(
      a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractScrollArea::dragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea13dragMoveEventEP14QDragMoveEvent(
    QAbstractScrollArea *self,
    QDragMoveEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::dragMoveEvent(
      a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractScrollArea::dragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea14dragLeaveEventEP15QDragLeaveEvent(
    QAbstractScrollArea *self,
    QDragLeaveEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::dragLeaveEvent(
      a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractScrollArea::dropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea9dropEventEP10QDropEvent(
    QAbstractScrollArea *self,
    QDropEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::dropEvent(
      a0);
}
#endif  // QT_CONFIG(draganddrop)

//  void QAbstractScrollArea::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea13keyPressEventEP9QKeyEvent(
    QAbstractScrollArea *self,
    QKeyEvent *a0) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::keyPressEvent(
      a0);
}

//  void QAbstractScrollArea::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractScrollArea16scrollContentsByEii(
    QAbstractScrollArea *self,
    int dx,
    int dy) {
  static_cast<OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::scrollContentsBy(
      dx,
      dy);
}

//  QSize QAbstractScrollArea::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QAbstractScrollArea16viewportSizeHintEv(
    const QAbstractScrollArea *self) {
  return new QSize(
      static_cast<const OwnQAbstractScrollArea *>(self)->OwnQAbstractScrollArea::viewportSizeHint());
}

#endif  // QT_CONFIG(scrollarea)
