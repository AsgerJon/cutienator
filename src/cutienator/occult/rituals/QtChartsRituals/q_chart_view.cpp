//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qchartview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCharts/qchartview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QChartView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQChartView : QChartView {
  using QChartView::resizeEvent;
  using QChartView::mousePressEvent;
  using QChartView::mouseMoveEvent;
  using QChartView::mouseReleaseEvent;
};

//  A QChartView that Python can take functions over in. Every QChartView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQChartViewCall0)(const void *, QResizeEvent *, int *);
typedef void (*CuteQChartViewCall1)(const void *, QMouseEvent *, int *);
typedef void (*CuteQChartViewCall2)(const void *, QMouseEvent *, int *);
typedef void (*CuteQChartViewCall3)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(graphicsview)
typedef const QSize * (*CuteQChartViewCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QVariant * (*CuteQChartViewCall5)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall6)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartViewCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartViewCall8)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall9)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall10)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall11)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall12)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall13)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall14)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQChartViewCall15)(const void *, bool, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall16)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall17)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall18)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall19)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall20)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall21)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall22)(const void *, int, int, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall23)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall24)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall25)(const void *, QPainter *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQChartViewCall26)(const void *, QPainter *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQChartViewCall27)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQChartViewCall28)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQChartViewCall29)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQChartViewCall30)(const void *, QEvent *, int *);
typedef void (*CuteQChartViewCall31)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQChartViewCall32)(const void *, int *);
typedef void (*CuteQChartViewCall33)(const void *, bool, int *);
typedef int (*CuteQChartViewCall34)(const void *, int, int *);
typedef bool (*CuteQChartViewCall35)(const void *, int *);
typedef void * (*CuteQChartViewCall36)(const void *, int *);
typedef void (*CuteQChartViewCall37)(const void *, QEnterEvent *, int *);
typedef void (*CuteQChartViewCall38)(const void *, QEvent *, int *);
typedef void (*CuteQChartViewCall39)(const void *, QMoveEvent *, int *);
typedef void (*CuteQChartViewCall40)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQChartViewCall41)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQChartViewCall42)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQChartViewCall43)(const void *, QHideEvent *, int *);
typedef int (*CuteQChartViewCall44)(const void *, int, int *);
typedef void (*CuteQChartViewCall45)(const void *, QPainter *, int *);
typedef void * (*CuteQChartViewCall46)(const void *, QPoint *, int *);
typedef void * (*CuteQChartViewCall47)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartViewCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartViewCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartViewCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartViewCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChartViewCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQChartView : public QChartView {
public:
  using QChartView::QChartView;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsView14drawBackgroundEP8QPainterRK6QRectF")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN13QGraphicsView14drawForegroundEP8QPainterRK6QRectF")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[40] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[47] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QChartView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQChartViewCall0 call = reinterpret_cast<CuteQChartViewCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QChartView::resizeEvent(event);
  }

  //  void QChartView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQChartViewCall1 call = reinterpret_cast<CuteQChartViewCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QChartView::mousePressEvent(event);
  }

  //  void QChartView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQChartViewCall2 call = reinterpret_cast<CuteQChartViewCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QChartView::mouseMoveEvent(event);
  }

  //  void QChartView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQChartViewCall3 call = reinterpret_cast<CuteQChartViewCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QChartView::mouseReleaseEvent(event);
  }

#if QT_CONFIG(graphicsview)
  //  QSize QGraphicsView::sizeHint() const
  QSize sizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQChartViewCall4 call = reinterpret_cast<CuteQChartViewCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsView::sizeHint();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QVariant QGraphicsView::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQChartViewCall5 call = reinterpret_cast<CuteQChartViewCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsView::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::setupViewport(QWidget *widget)
  void setupViewport(QWidget *widget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQChartViewCall6 call = reinterpret_cast<CuteQChartViewCall6>(taken[6]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QGraphicsView::setupViewport(widget);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsView::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQChartViewCall7 call = reinterpret_cast<CuteQChartViewCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsView::event(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQChartViewCall8 call = reinterpret_cast<CuteQChartViewCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsView::viewportEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQChartViewCall9 call = reinterpret_cast<CuteQChartViewCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::contextMenuEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQChartViewCall10 call = reinterpret_cast<CuteQChartViewCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQChartViewCall11 call = reinterpret_cast<CuteQChartViewCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQChartViewCall12 call = reinterpret_cast<CuteQChartViewCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQChartViewCall13 call = reinterpret_cast<CuteQChartViewCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::dropEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQChartViewCall14 call = reinterpret_cast<CuteQChartViewCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::focusInEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[15]) {
      int handled = 0;
      CuteQChartViewCall15 call = reinterpret_cast<CuteQChartViewCall15>(taken[15]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QGraphicsView::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQChartViewCall16 call = reinterpret_cast<CuteQChartViewCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::focusOutEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQChartViewCall17 call = reinterpret_cast<CuteQChartViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::keyPressEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQChartViewCall18 call = reinterpret_cast<CuteQChartViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQChartViewCall19 call = reinterpret_cast<CuteQChartViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQChartViewCall20 call = reinterpret_cast<CuteQChartViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::wheelEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQChartViewCall21 call = reinterpret_cast<CuteQChartViewCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::paintEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[22]) {
      int handled = 0;
      CuteQChartViewCall22 call = reinterpret_cast<CuteQChartViewCall22>(taken[22]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QGraphicsView::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQChartViewCall23 call = reinterpret_cast<CuteQChartViewCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::showEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQChartViewCall24 call = reinterpret_cast<CuteQChartViewCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::drawBackground(QPainter *painter, const QRectF
  //      &rect)
  void drawBackground(QPainter *painter, const QRectF &rect) override {
    if (taken[25]) {
      int handled = 0;
      CuteQChartViewCall25 call = reinterpret_cast<CuteQChartViewCall25>(taken[25]);
      call(this, painter, &rect, &handled);
      if (handled) return;
    }
    QGraphicsView::drawBackground(painter, rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsView::drawForeground(QPainter *painter, const QRectF
  //      &rect)
  void drawForeground(QPainter *painter, const QRectF &rect) override {
    if (taken[26]) {
      int handled = 0;
      CuteQChartViewCall26 call = reinterpret_cast<CuteQChartViewCall26>(taken[26]);
      call(this, painter, &rect, &handled);
      if (handled) return;
    }
    QGraphicsView::drawForeground(painter, rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQChartViewCall27 call = reinterpret_cast<CuteQChartViewCall27>(taken[27]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[28]) {
      int handled = 0;
      CuteQChartViewCall28 call = reinterpret_cast<CuteQChartViewCall28>(taken[28]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQChartViewCall29 call = reinterpret_cast<CuteQChartViewCall29>(taken[29]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::viewportSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQChartViewCall30 call = reinterpret_cast<CuteQChartViewCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQChartViewCall31 call = reinterpret_cast<CuteQChartViewCall31>(taken[31]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQChartViewCall32 call = reinterpret_cast<CuteQChartViewCall32>(taken[32]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[33]) {
      int handled = 0;
      CuteQChartViewCall33 call = reinterpret_cast<CuteQChartViewCall33>(taken[33]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQChartViewCall34 call = reinterpret_cast<CuteQChartViewCall34>(taken[34]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQChartViewCall35 call = reinterpret_cast<CuteQChartViewCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQChartViewCall36 call = reinterpret_cast<CuteQChartViewCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQChartViewCall37 call = reinterpret_cast<CuteQChartViewCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQChartViewCall38 call = reinterpret_cast<CuteQChartViewCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQChartViewCall39 call = reinterpret_cast<CuteQChartViewCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQChartViewCall40 call = reinterpret_cast<CuteQChartViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQChartViewCall41 call = reinterpret_cast<CuteQChartViewCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQChartViewCall42 call = reinterpret_cast<CuteQChartViewCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQChartViewCall43 call = reinterpret_cast<CuteQChartViewCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQChartViewCall44 call = reinterpret_cast<CuteQChartViewCall44>(taken[44]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQChartViewCall45 call = reinterpret_cast<CuteQChartViewCall45>(taken[45]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQChartViewCall46 call = reinterpret_cast<CuteQChartViewCall46>(taken[46]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[47]) {
      int handled = 0;
      CuteQChartViewCall47 call = reinterpret_cast<CuteQChartViewCall47>(taken[47]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQChartViewCall48 call = reinterpret_cast<CuteQChartViewCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQChartViewCall49 call = reinterpret_cast<CuteQChartViewCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQChartViewCall50 call = reinterpret_cast<CuteQChartViewCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQChartViewCall51 call = reinterpret_cast<CuteQChartViewCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQChartViewCall52 call = reinterpret_cast<CuteQChartViewCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QChartView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QChartView10metaObjectEv(
    const QChartView *self) {
  return self->metaObject();
}

//  QString QChartView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QChartView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QChartView::tr(s, c, n));
}

//  QChartView::QChartView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QChartView *ritual_ZN10QChartViewC1EP7QWidget(QWidget *parent) {
  return new CuteQChartView(parent);
}

//  QChartView::QChartView(QChart *chart, QWidget *parent)
extern "C" Q_DECL_EXPORT
QChartView *ritual_ZN10QChartViewC1EP6QChartP7QWidget(
    QChart *chart,
    QWidget *parent) {
  return new CuteQChartView(chart, parent);
}

//  QChartView::~QChartView()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QChartViewD1Ev(QChartView *self) {
  delete self;
}

//  RubberBands QChartView::rubberBand() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QChartView10rubberBandEv(const QChartView *self) {
  return static_cast<int>(self->rubberBand().toInt());
}

//  QChart *QChartView::chart() const
extern "C" Q_DECL_EXPORT
QChart *ritual_ZNK10QChartView5chartEv(const QChartView *self) {
  return self->chart();
}

//  void QChartView::setChart(QChart *chart)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QChartView8setChartEP6QChart(
    QChartView *self,
    QChart *chart) {
  self->setChart(chart);
}

//  void QChartView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QChartView11resizeEventEP12QResizeEvent(
    QChartView *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QChartView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QChartView15mousePressEventEP11QMouseEvent(
    QChartView *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QChartView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QChartView14mouseMoveEventEP11QMouseEvent(
    QChartView *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QChartView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QChartView17mouseReleaseEventEP11QMouseEvent(
    QChartView *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  a Python function taken by a CuteQChartView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QChartView(QChartView *self, const char *key, void *call) {
  return static_cast<CuteQChartView *>(self)->take(key, call);
}

//  void QChartView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QChartView11resizeEventEP12QResizeEvent(
    QChartView *self,
    QResizeEvent *event) {
  static_cast<OwnQChartView *>(self)->OwnQChartView::resizeEvent(event);
}

//  void QChartView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QChartView15mousePressEventEP11QMouseEvent(
    QChartView *self,
    QMouseEvent *event) {
  static_cast<OwnQChartView *>(self)->OwnQChartView::mousePressEvent(event);
}

//  void QChartView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QChartView14mouseMoveEventEP11QMouseEvent(
    QChartView *self,
    QMouseEvent *event) {
  static_cast<OwnQChartView *>(self)->OwnQChartView::mouseMoveEvent(event);
}

//  void QChartView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QChartView17mouseReleaseEventEP11QMouseEvent(
    QChartView *self,
    QMouseEvent *event) {
  static_cast<OwnQChartView *>(self)->OwnQChartView::mouseReleaseEvent(
      event);
}
