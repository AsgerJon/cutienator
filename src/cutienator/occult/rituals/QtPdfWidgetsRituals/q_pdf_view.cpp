//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdfWidgets/qpdfview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtPdfWidgets/qpdfview.h>
#include <QtCore/qstring.h>
#include <QtCore/qmargins.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QPdfView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPdfView : QPdfView {
  using QPdfView::paintEvent;
  using QPdfView::resizeEvent;
  using QPdfView::scrollContentsBy;
  using QPdfView::mousePressEvent;
  using QPdfView::mouseMoveEvent;
  using QPdfView::mouseReleaseEvent;
  using QPdfView::wheelEvent;
};

//  A QPdfView that Python can take functions over in. Every QPdfView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPdfViewCall0)(const void *, QPaintEvent *, int *);
typedef void (*CuteQPdfViewCall1)(const void *, QResizeEvent *, int *);
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall3)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPdfViewCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPdfViewCall5)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQPdfViewCall6)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQPdfViewCall7)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQPdfViewCall8)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall9)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQPdfViewCall10)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQPdfViewCall11)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQPdfViewCall12)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall13)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall15)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall16)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall17)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall18)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall19)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQPdfViewCall20)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQPdfViewCall21)(const void *, QEvent *, int *);
typedef void (*CuteQPdfViewCall22)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQPdfViewCall23)(const void *, int *);
typedef void (*CuteQPdfViewCall24)(const void *, bool, int *);
typedef int (*CuteQPdfViewCall25)(const void *, int, int *);
typedef bool (*CuteQPdfViewCall26)(const void *, int *);
typedef void * (*CuteQPdfViewCall27)(const void *, int *);
typedef void (*CuteQPdfViewCall28)(const void *, QKeyEvent *, int *);
typedef void (*CuteQPdfViewCall29)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPdfViewCall30)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPdfViewCall31)(const void *, QEnterEvent *, int *);
typedef void (*CuteQPdfViewCall32)(const void *, QEvent *, int *);
typedef void (*CuteQPdfViewCall33)(const void *, QMoveEvent *, int *);
typedef void (*CuteQPdfViewCall34)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQPdfViewCall35)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQPdfViewCall36)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQPdfViewCall37)(const void *, QShowEvent *, int *);
typedef void (*CuteQPdfViewCall38)(const void *, QHideEvent *, int *);
typedef int (*CuteQPdfViewCall39)(const void *, int, int *);
typedef void (*CuteQPdfViewCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQPdfViewCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQPdfViewCall42)(const void *, int *);
typedef void (*CuteQPdfViewCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQPdfViewCall44)(const void *, int, int *);
typedef bool (*CuteQPdfViewCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfViewCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfViewCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfViewCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfViewCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfViewCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPdfView : public QPdfView {
public:
  using QPdfView::QPdfView;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[1] = call;
      return true;
    }
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
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

  //  void QPdfView::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPdfViewCall0 call = reinterpret_cast<CuteQPdfViewCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QPdfView::paintEvent(event);
  }

  //  void QPdfView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPdfViewCall1 call = reinterpret_cast<CuteQPdfViewCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QPdfView::resizeEvent(event);
  }

#if QT_CONFIG(scrollarea)
  //  void QPdfView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPdfViewCall2 call = reinterpret_cast<CuteQPdfViewCall2>(taken[2]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QPdfView::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QPdfView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPdfViewCall3 call = reinterpret_cast<CuteQPdfViewCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QPdfView::mousePressEvent(event);
  }

  //  void QPdfView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPdfViewCall4 call = reinterpret_cast<CuteQPdfViewCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QPdfView::mouseMoveEvent(event);
  }

  //  void QPdfView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPdfViewCall5 call = reinterpret_cast<CuteQPdfViewCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QPdfView::mouseReleaseEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QPdfView::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPdfViewCall6 call = reinterpret_cast<CuteQPdfViewCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QPdfView::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPdfViewCall7 call = reinterpret_cast<CuteQPdfViewCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPdfViewCall8 call = reinterpret_cast<CuteQPdfViewCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPdfViewCall9 call = reinterpret_cast<CuteQPdfViewCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQPdfViewCall10 call = reinterpret_cast<CuteQPdfViewCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQPdfViewCall11 call = reinterpret_cast<CuteQPdfViewCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQPdfViewCall12 call = reinterpret_cast<CuteQPdfViewCall12>(taken[12]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::viewportEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPdfViewCall13 call = reinterpret_cast<CuteQPdfViewCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::mouseDoubleClickEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPdfViewCall14 call = reinterpret_cast<CuteQPdfViewCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQPdfViewCall15 call = reinterpret_cast<CuteQPdfViewCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQPdfViewCall16 call = reinterpret_cast<CuteQPdfViewCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQPdfViewCall17 call = reinterpret_cast<CuteQPdfViewCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQPdfViewCall18 call = reinterpret_cast<CuteQPdfViewCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQPdfViewCall19 call = reinterpret_cast<CuteQPdfViewCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQPdfViewCall20 call = reinterpret_cast<CuteQPdfViewCall20>(taken[20]);
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
      CuteQPdfViewCall21 call = reinterpret_cast<CuteQPdfViewCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQPdfViewCall22 call = reinterpret_cast<CuteQPdfViewCall22>(taken[22]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQPdfViewCall23 call = reinterpret_cast<CuteQPdfViewCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[24]) {
      int handled = 0;
      CuteQPdfViewCall24 call = reinterpret_cast<CuteQPdfViewCall24>(taken[24]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQPdfViewCall25 call = reinterpret_cast<CuteQPdfViewCall25>(taken[25]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQPdfViewCall26 call = reinterpret_cast<CuteQPdfViewCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQPdfViewCall27 call = reinterpret_cast<CuteQPdfViewCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQPdfViewCall28 call = reinterpret_cast<CuteQPdfViewCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQPdfViewCall29 call = reinterpret_cast<CuteQPdfViewCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQPdfViewCall30 call = reinterpret_cast<CuteQPdfViewCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQPdfViewCall31 call = reinterpret_cast<CuteQPdfViewCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQPdfViewCall32 call = reinterpret_cast<CuteQPdfViewCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQPdfViewCall33 call = reinterpret_cast<CuteQPdfViewCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQPdfViewCall34 call = reinterpret_cast<CuteQPdfViewCall34>(taken[34]);
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
      CuteQPdfViewCall35 call = reinterpret_cast<CuteQPdfViewCall35>(taken[35]);
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
      CuteQPdfViewCall36 call = reinterpret_cast<CuteQPdfViewCall36>(taken[36]);
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
      CuteQPdfViewCall37 call = reinterpret_cast<CuteQPdfViewCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQPdfViewCall38 call = reinterpret_cast<CuteQPdfViewCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQPdfViewCall39 call = reinterpret_cast<CuteQPdfViewCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQPdfViewCall40 call = reinterpret_cast<CuteQPdfViewCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQPdfViewCall41 call = reinterpret_cast<CuteQPdfViewCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQPdfViewCall42 call = reinterpret_cast<CuteQPdfViewCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQPdfViewCall43 call = reinterpret_cast<CuteQPdfViewCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQPdfViewCall44 call = reinterpret_cast<CuteQPdfViewCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQPdfViewCall45 call = reinterpret_cast<CuteQPdfViewCall45>(taken[45]);
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
      CuteQPdfViewCall46 call = reinterpret_cast<CuteQPdfViewCall46>(taken[46]);
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
      CuteQPdfViewCall47 call = reinterpret_cast<CuteQPdfViewCall47>(taken[47]);
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
      CuteQPdfViewCall48 call = reinterpret_cast<CuteQPdfViewCall48>(taken[48]);
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
      CuteQPdfViewCall49 call = reinterpret_cast<CuteQPdfViewCall49>(taken[49]);
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
      CuteQPdfViewCall50 call = reinterpret_cast<CuteQPdfViewCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPdfView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QPdfView10metaObjectEv(const QPdfView *self) {
  return self->metaObject();
}

//  void *QPdfView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8QPdfView11qt_metacastEPKc(QPdfView *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPdfView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QPdfView11qt_metacallEN11QMetaObject4CallEiPPv(
    QPdfView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPdfView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QPdfView2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QPdfView::tr(s, c, n));
}

//  QPdfView::QPdfView()
extern "C" Q_DECL_EXPORT
QPdfView *ritual_ZN8QPdfViewC1Ev() {
  return new CuteQPdfView();
}

//  QPdfView::QPdfView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QPdfView *ritual_ZN8QPdfViewC1EP7QWidget(QWidget *parent) {
  return new CuteQPdfView(parent);
}

//  QPdfView::~QPdfView()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfViewD1Ev(QPdfView *self) {
  delete self;
}

//  void QPdfView::setDocument(QPdfDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView11setDocumentEP12QPdfDocument(
    QPdfView *self,
    QPdfDocument *document) {
  self->setDocument(document);
}

//  QPdfDocument *QPdfView::document() const
extern "C" Q_DECL_EXPORT
QPdfDocument *ritual_ZNK8QPdfView8documentEv(const QPdfView *self) {
  return self->document();
}

//  QPdfSearchModel *QPdfView::searchModel() const
extern "C" Q_DECL_EXPORT
QPdfSearchModel *ritual_ZNK8QPdfView11searchModelEv(const QPdfView *self) {
  return self->searchModel();
}

//  void QPdfView::setSearchModel(QPdfSearchModel *searchModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView14setSearchModelEP15QPdfSearchModel(
    QPdfView *self,
    QPdfSearchModel *searchModel) {
  self->setSearchModel(searchModel);
}

//  int QPdfView::currentSearchResultIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPdfView24currentSearchResultIndexEv(const QPdfView *self) {
  return self->currentSearchResultIndex();
}

//  QPdfPageNavigator *QPdfView::pageNavigator() const
extern "C" Q_DECL_EXPORT
QPdfPageNavigator *ritual_ZNK8QPdfView13pageNavigatorEv(
    const QPdfView *self) {
  return self->pageNavigator();
}

//  PageMode QPdfView::pageMode() const
extern "C" Q_DECL_EXPORT
QPdfView::PageMode ritual_ZNK8QPdfView8pageModeEv(const QPdfView *self) {
  return self->pageMode();
}

//  ZoomMode QPdfView::zoomMode() const
extern "C" Q_DECL_EXPORT
QPdfView::ZoomMode ritual_ZNK8QPdfView8zoomModeEv(const QPdfView *self) {
  return self->zoomMode();
}

//  qreal QPdfView::zoomFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QPdfView10zoomFactorEv(const QPdfView *self) {
  return self->zoomFactor();
}

//  int QPdfView::pageSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QPdfView11pageSpacingEv(const QPdfView *self) {
  return self->pageSpacing();
}

//  void QPdfView::setPageSpacing(int spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView14setPageSpacingEi(QPdfView *self, int spacing) {
  self->setPageSpacing(spacing);
}

//  QMargins QPdfView::documentMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK8QPdfView15documentMarginsEv(const QPdfView *self) {
  return new QMargins(self->documentMargins());
}

//  void QPdfView::setDocumentMargins(QMargins margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView18setDocumentMarginsE8QMargins(
    QPdfView *self,
    const QMargins *margins) {
  self->setDocumentMargins(*margins);
}

//  void QPdfView::setPageMode(QPdfView::PageMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView11setPageModeENS_8PageModeE(
    QPdfView *self,
    QPdfView::PageMode mode) {
  self->setPageMode(mode);
}

//  void QPdfView::setZoomMode(QPdfView::ZoomMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView11setZoomModeENS_8ZoomModeE(
    QPdfView *self,
    QPdfView::ZoomMode mode) {
  self->setZoomMode(mode);
}

//  void QPdfView::setZoomFactor(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView13setZoomFactorEd(QPdfView *self, qreal factor) {
  self->setZoomFactor(factor);
}

//  void QPdfView::setCurrentSearchResultIndex(int currentResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView27setCurrentSearchResultIndexEi(
    QPdfView *self,
    int currentResult) {
  self->setCurrentSearchResultIndex(currentResult);
}

//  void QPdfView::documentChanged(QPdfDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView15documentChangedEP12QPdfDocument(
    QPdfView *self,
    QPdfDocument *document) {
  self->documentChanged(document);
}

//  void QPdfView::pageModeChanged(QPdfView::PageMode pageMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView15pageModeChangedENS_8PageModeE(
    QPdfView *self,
    QPdfView::PageMode pageMode) {
  self->pageModeChanged(pageMode);
}

//  void QPdfView::zoomModeChanged(QPdfView::ZoomMode zoomMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView15zoomModeChangedENS_8ZoomModeE(
    QPdfView *self,
    QPdfView::ZoomMode zoomMode) {
  self->zoomModeChanged(zoomMode);
}

//  void QPdfView::zoomFactorChanged(qreal zoomFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView17zoomFactorChangedEd(
    QPdfView *self,
    qreal zoomFactor) {
  self->zoomFactorChanged(zoomFactor);
}

//  void QPdfView::pageSpacingChanged(int pageSpacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView18pageSpacingChangedEi(
    QPdfView *self,
    int pageSpacing) {
  self->pageSpacingChanged(pageSpacing);
}

//  void QPdfView::documentMarginsChanged(QMargins documentMargins)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView22documentMarginsChangedE8QMargins(
    QPdfView *self,
    const QMargins *documentMargins) {
  self->documentMarginsChanged(*documentMargins);
}

//  void QPdfView::searchModelChanged(QPdfSearchModel *searchModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView18searchModelChangedEP15QPdfSearchModel(
    QPdfView *self,
    QPdfSearchModel *searchModel) {
  self->searchModelChanged(searchModel);
}

//  void QPdfView::currentSearchResultIndexChanged(int currentResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView31currentSearchResultIndexChangedEi(
    QPdfView *self,
    int currentResult) {
  self->currentSearchResultIndexChanged(currentResult);
}

//  void QPdfView::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView10paintEventEP11QPaintEvent(
    QPdfView *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QPdfView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView11resizeEventEP12QResizeEvent(
    QPdfView *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QPdfView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView16scrollContentsByEii(
    QPdfView *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  void QPdfView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView15mousePressEventEP11QMouseEvent(
    QPdfView *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QPdfView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView14mouseMoveEventEP11QMouseEvent(
    QPdfView *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QPdfView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView17mouseReleaseEventEP11QMouseEvent(
    QPdfView *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QPdfView::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfView10wheelEventEP11QWheelEvent(
    QPdfView *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}

//  QPdfViewPrivate *QPdfView::d_func()
extern "C" Q_DECL_EXPORT
QPdfViewPrivate *ritual_ZN8QPdfView6d_funcEv(QPdfView *self) {
  return self->d_func();
}

//  const QPdfViewPrivate *QPdfView::d_func() const
extern "C" Q_DECL_EXPORT
const QPdfViewPrivate *ritual_ZNK8QPdfView6d_funcEv(const QPdfView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPdfView, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfView(QPdfView *self, const char *key, void *call) {
  return static_cast<CuteQPdfView *>(self)->take(key, call);
}

//  void QPdfView::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QPdfView10paintEventEP11QPaintEvent(
    QPdfView *self,
    QPaintEvent *event) {
  static_cast<OwnQPdfView *>(self)->OwnQPdfView::paintEvent(event);
}

//  void QPdfView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QPdfView11resizeEventEP12QResizeEvent(
    QPdfView *self,
    QResizeEvent *event) {
  static_cast<OwnQPdfView *>(self)->OwnQPdfView::resizeEvent(event);
}

//  void QPdfView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QPdfView16scrollContentsByEii(
    QPdfView *self,
    int dx,
    int dy) {
  static_cast<OwnQPdfView *>(self)->OwnQPdfView::scrollContentsBy(dx, dy);
}

//  void QPdfView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QPdfView15mousePressEventEP11QMouseEvent(
    QPdfView *self,
    QMouseEvent *event) {
  static_cast<OwnQPdfView *>(self)->OwnQPdfView::mousePressEvent(event);
}

//  void QPdfView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QPdfView14mouseMoveEventEP11QMouseEvent(
    QPdfView *self,
    QMouseEvent *event) {
  static_cast<OwnQPdfView *>(self)->OwnQPdfView::mouseMoveEvent(event);
}

//  void QPdfView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QPdfView17mouseReleaseEventEP11QMouseEvent(
    QPdfView *self,
    QMouseEvent *event) {
  static_cast<OwnQPdfView *>(self)->OwnQPdfView::mouseReleaseEvent(event);
}

//  void QPdfView::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QPdfView10wheelEventEP11QWheelEvent(
    QPdfView *self,
    QWheelEvent *event) {
  static_cast<OwnQPdfView *>(self)->OwnQPdfView::wheelEvent(event);
}
