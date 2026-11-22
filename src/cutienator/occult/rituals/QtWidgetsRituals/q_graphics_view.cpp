//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qvariant.h>
#include <QtGui/qbrush.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsView : QGraphicsView {
  using QGraphicsView::setupViewport;
  using QGraphicsView::event;
  using QGraphicsView::viewportEvent;
  using QGraphicsView::contextMenuEvent;
  using QGraphicsView::dragEnterEvent;
  using QGraphicsView::dragLeaveEvent;
  using QGraphicsView::dragMoveEvent;
  using QGraphicsView::dropEvent;
  using QGraphicsView::focusInEvent;
  using QGraphicsView::focusNextPrevChild;
  using QGraphicsView::focusOutEvent;
  using QGraphicsView::keyPressEvent;
  using QGraphicsView::keyReleaseEvent;
  using QGraphicsView::mouseDoubleClickEvent;
  using QGraphicsView::mousePressEvent;
  using QGraphicsView::mouseMoveEvent;
  using QGraphicsView::mouseReleaseEvent;
  using QGraphicsView::wheelEvent;
  using QGraphicsView::paintEvent;
  using QGraphicsView::resizeEvent;
  using QGraphicsView::scrollContentsBy;
  using QGraphicsView::showEvent;
  using QGraphicsView::inputMethodEvent;
  using QGraphicsView::drawBackground;
  using QGraphicsView::drawForeground;
};

//  A QGraphicsView that Python can take functions over in. Every QGraphicsView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQGraphicsViewCall0)(const void *, int *);
typedef const QVariant * (*CuteQGraphicsViewCall1)(const void *, int, int *);
typedef void (*CuteQGraphicsViewCall2)(const void *, QWidget *, int *);
typedef bool (*CuteQGraphicsViewCall3)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsViewCall4)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsViewCall5)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQGraphicsViewCall6)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQGraphicsViewCall7)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQGraphicsViewCall8)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQGraphicsViewCall9)(const void *, QDropEvent *, int *);
typedef void (*CuteQGraphicsViewCall10)(const void *, QFocusEvent *, int *);
typedef bool (*CuteQGraphicsViewCall11)(const void *, bool, int *);
typedef void (*CuteQGraphicsViewCall12)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsViewCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsViewCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsViewCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphicsViewCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphicsViewCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphicsViewCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphicsViewCall19)(const void *, QWheelEvent *, int *);
typedef void (*CuteQGraphicsViewCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQGraphicsViewCall21)(const void *, QResizeEvent *, int *);
typedef void (*CuteQGraphicsViewCall22)(const void *, int, int, int *);
typedef void (*CuteQGraphicsViewCall23)(const void *, QShowEvent *, int *);
typedef void (*CuteQGraphicsViewCall24)(const void *, QInputMethodEvent *, int *);
typedef void (*CuteQGraphicsViewCall25)(const void *, QPainter *, const QRectF *, int *);
typedef void (*CuteQGraphicsViewCall26)(const void *, QPainter *, const QRectF *, int *);
typedef const QSize * (*CuteQGraphicsViewCall27)(const void *, int *);
typedef bool (*CuteQGraphicsViewCall28)(const void *, QObject *, QEvent *, int *);
typedef const QSize * (*CuteQGraphicsViewCall29)(const void *, int *);
typedef void (*CuteQGraphicsViewCall30)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsViewCall31)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQGraphicsViewCall32)(const void *, int *);
typedef void (*CuteQGraphicsViewCall33)(const void *, bool, int *);
typedef int (*CuteQGraphicsViewCall34)(const void *, int, int *);
typedef bool (*CuteQGraphicsViewCall35)(const void *, int *);
typedef void * (*CuteQGraphicsViewCall36)(const void *, int *);
typedef void (*CuteQGraphicsViewCall37)(const void *, QEnterEvent *, int *);
typedef void (*CuteQGraphicsViewCall38)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsViewCall39)(const void *, QMoveEvent *, int *);
typedef void (*CuteQGraphicsViewCall40)(const void *, QCloseEvent *, int *);
typedef void (*CuteQGraphicsViewCall41)(const void *, QTabletEvent *, int *);
typedef void (*CuteQGraphicsViewCall42)(const void *, QActionEvent *, int *);
typedef void (*CuteQGraphicsViewCall43)(const void *, QHideEvent *, int *);
typedef int (*CuteQGraphicsViewCall44)(const void *, int, int *);
typedef void (*CuteQGraphicsViewCall45)(const void *, QPainter *, int *);
typedef void * (*CuteQGraphicsViewCall46)(const void *, QPoint *, int *);
typedef void * (*CuteQGraphicsViewCall47)(const void *, int *);
typedef void (*CuteQGraphicsViewCall48)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsViewCall49)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsViewCall50)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsViewCall51)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsViewCall52)(const void *, const QMetaMethod *, int *);
class CuteQGraphicsView : public QGraphicsView {
public:
  using QGraphicsView::QGraphicsView;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
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
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsView14drawBackgroundEP8QPainterRK6QRectF")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QGraphicsView14drawForegroundEP8QPainterRK6QRectF")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[29] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[42] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
    return false;
  }

  //  QSize QGraphicsView::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsViewCall0 call = reinterpret_cast<CuteQGraphicsViewCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsView::sizeHint();
  }

  //  QVariant QGraphicsView::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsViewCall1 call = reinterpret_cast<CuteQGraphicsViewCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsView::inputMethodQuery(query);
  }

  //  void QGraphicsView::setupViewport(QWidget *widget)
  void setupViewport(QWidget *widget) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsViewCall2 call = reinterpret_cast<CuteQGraphicsViewCall2>(taken[2]);
      call(this, widget, &handled);
      if (handled) return;
    }
    QGraphicsView::setupViewport(widget);
  }

  //  bool QGraphicsView::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsViewCall3 call = reinterpret_cast<CuteQGraphicsViewCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsView::event(event);
  }

  //  bool QGraphicsView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsViewCall4 call = reinterpret_cast<CuteQGraphicsViewCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsView::viewportEvent(event);
  }

  //  void QGraphicsView::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsViewCall5 call = reinterpret_cast<CuteQGraphicsViewCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::contextMenuEvent(event);
  }

  //  void QGraphicsView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsViewCall6 call = reinterpret_cast<CuteQGraphicsViewCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::dragEnterEvent(event);
  }

  //  void QGraphicsView::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsViewCall7 call = reinterpret_cast<CuteQGraphicsViewCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::dragLeaveEvent(event);
  }

  //  void QGraphicsView::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsViewCall8 call = reinterpret_cast<CuteQGraphicsViewCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::dragMoveEvent(event);
  }

  //  void QGraphicsView::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsViewCall9 call = reinterpret_cast<CuteQGraphicsViewCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::dropEvent(event);
  }

  //  void QGraphicsView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsViewCall10 call = reinterpret_cast<CuteQGraphicsViewCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::focusInEvent(event);
  }

  //  bool QGraphicsView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsViewCall11 call = reinterpret_cast<CuteQGraphicsViewCall11>(taken[11]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QGraphicsView::focusNextPrevChild(next);
  }

  //  void QGraphicsView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsViewCall12 call = reinterpret_cast<CuteQGraphicsViewCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::focusOutEvent(event);
  }

  //  void QGraphicsView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsViewCall13 call = reinterpret_cast<CuteQGraphicsViewCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::keyPressEvent(event);
  }

  //  void QGraphicsView::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsViewCall14 call = reinterpret_cast<CuteQGraphicsViewCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::keyReleaseEvent(event);
  }

  //  void QGraphicsView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsViewCall15 call = reinterpret_cast<CuteQGraphicsViewCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::mouseDoubleClickEvent(event);
  }

  //  void QGraphicsView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsViewCall16 call = reinterpret_cast<CuteQGraphicsViewCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::mousePressEvent(event);
  }

  //  void QGraphicsView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsViewCall17 call = reinterpret_cast<CuteQGraphicsViewCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::mouseMoveEvent(event);
  }

  //  void QGraphicsView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsViewCall18 call = reinterpret_cast<CuteQGraphicsViewCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::mouseReleaseEvent(event);
  }

  //  void QGraphicsView::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsViewCall19 call = reinterpret_cast<CuteQGraphicsViewCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::wheelEvent(event);
  }

  //  void QGraphicsView::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsViewCall20 call = reinterpret_cast<CuteQGraphicsViewCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::paintEvent(event);
  }

  //  void QGraphicsView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsViewCall21 call = reinterpret_cast<CuteQGraphicsViewCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::resizeEvent(event);
  }

  //  void QGraphicsView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsViewCall22 call = reinterpret_cast<CuteQGraphicsViewCall22>(taken[22]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QGraphicsView::scrollContentsBy(dx, dy);
  }

  //  void QGraphicsView::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsViewCall23 call = reinterpret_cast<CuteQGraphicsViewCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::showEvent(event);
  }

  //  void QGraphicsView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsViewCall24 call = reinterpret_cast<CuteQGraphicsViewCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsView::inputMethodEvent(event);
  }

  //  void QGraphicsView::drawBackground(QPainter *painter, const QRectF
  //      &rect)
  void drawBackground(QPainter *painter, const QRectF &rect) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsViewCall25 call = reinterpret_cast<CuteQGraphicsViewCall25>(taken[25]);
      call(this, painter, &rect, &handled);
      if (handled) return;
    }
    QGraphicsView::drawBackground(painter, rect);
  }

  //  void QGraphicsView::drawForeground(QPainter *painter, const QRectF
  //      &rect)
  void drawForeground(QPainter *painter, const QRectF &rect) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsViewCall26 call = reinterpret_cast<CuteQGraphicsViewCall26>(taken[26]);
      call(this, painter, &rect, &handled);
      if (handled) return;
    }
    QGraphicsView::drawForeground(painter, rect);
  }

  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphicsViewCall27 call = reinterpret_cast<CuteQGraphicsViewCall27>(taken[27]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }

  //  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphicsViewCall28 call = reinterpret_cast<CuteQGraphicsViewCall28>(taken[28]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::eventFilter(a0, a1);
  }

  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphicsViewCall29 call = reinterpret_cast<CuteQGraphicsViewCall29>(taken[29]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::viewportSizeHint();
  }

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphicsViewCall30 call = reinterpret_cast<CuteQGraphicsViewCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQGraphicsViewCall31 call = reinterpret_cast<CuteQGraphicsViewCall31>(taken[31]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQGraphicsViewCall32 call = reinterpret_cast<CuteQGraphicsViewCall32>(taken[32]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[33]) {
      int handled = 0;
      CuteQGraphicsViewCall33 call = reinterpret_cast<CuteQGraphicsViewCall33>(taken[33]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQGraphicsViewCall34 call = reinterpret_cast<CuteQGraphicsViewCall34>(taken[34]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQGraphicsViewCall35 call = reinterpret_cast<CuteQGraphicsViewCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQGraphicsViewCall36 call = reinterpret_cast<CuteQGraphicsViewCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQGraphicsViewCall37 call = reinterpret_cast<CuteQGraphicsViewCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQGraphicsViewCall38 call = reinterpret_cast<CuteQGraphicsViewCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQGraphicsViewCall39 call = reinterpret_cast<CuteQGraphicsViewCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQGraphicsViewCall40 call = reinterpret_cast<CuteQGraphicsViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQGraphicsViewCall41 call = reinterpret_cast<CuteQGraphicsViewCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQGraphicsViewCall42 call = reinterpret_cast<CuteQGraphicsViewCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQGraphicsViewCall43 call = reinterpret_cast<CuteQGraphicsViewCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQGraphicsViewCall44 call = reinterpret_cast<CuteQGraphicsViewCall44>(taken[44]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQGraphicsViewCall45 call = reinterpret_cast<CuteQGraphicsViewCall45>(taken[45]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQGraphicsViewCall46 call = reinterpret_cast<CuteQGraphicsViewCall46>(taken[46]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[47]) {
      int handled = 0;
      CuteQGraphicsViewCall47 call = reinterpret_cast<CuteQGraphicsViewCall47>(taken[47]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQGraphicsViewCall48 call = reinterpret_cast<CuteQGraphicsViewCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQGraphicsViewCall49 call = reinterpret_cast<CuteQGraphicsViewCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQGraphicsViewCall50 call = reinterpret_cast<CuteQGraphicsViewCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQGraphicsViewCall51 call = reinterpret_cast<CuteQGraphicsViewCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQGraphicsViewCall52 call = reinterpret_cast<CuteQGraphicsViewCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGraphicsView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QGraphicsView10metaObjectEv(
    const QGraphicsView *self) {
  return self->metaObject();
}

//  QString QGraphicsView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QGraphicsView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsView::tr(s, c, n));
}

//  QGraphicsView::QGraphicsView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QGraphicsView *ritual_ZN13QGraphicsViewC1EP7QWidget(QWidget *parent) {
  return new CuteQGraphicsView(parent);
}

//  QGraphicsView::QGraphicsView(QGraphicsScene *scene, QWidget *parent)
extern "C" Q_DECL_EXPORT
QGraphicsView *ritual_ZN13QGraphicsViewC1EP14QGraphicsSceneP7QWidget(
    QGraphicsScene *scene,
    QWidget *parent) {
  return new CuteQGraphicsView(scene, parent);
}

//  QGraphicsView::~QGraphicsView()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsViewD1Ev(QGraphicsView *self) {
  delete self;
}

//  QSize QGraphicsView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QGraphicsView8sizeHintEv(const QGraphicsView *self) {
  return new QSize(self->sizeHint());
}

//  QPainter::RenderHints QGraphicsView::renderHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsView11renderHintsEv(const QGraphicsView *self) {
  return static_cast<int>(self->renderHints().toInt());
}

//  void QGraphicsView::setRenderHint(QPainter::RenderHint hint, bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView13setRenderHintEN8QPainter10RenderHintEb(
    QGraphicsView *self,
    QPainter::RenderHint hint,
    bool enabled) {
  self->setRenderHint(hint, enabled);
}

//  void QGraphicsView::setRenderHints(QPainter::RenderHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView14setRenderHintsE6QFlagsIN8QPainter10RenderHintEE(
    QGraphicsView *self,
    int hints) {
  self->setRenderHints(QFlags<QPainter::RenderHint>::fromInt(hints));
}

//  Qt::Alignment QGraphicsView::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsView9alignmentEv(const QGraphicsView *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QGraphicsView::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsView *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  ViewportAnchor QGraphicsView::transformationAnchor() const
extern "C" Q_DECL_EXPORT
QGraphicsView::ViewportAnchor ritual_ZNK13QGraphicsView20transformationAnchorEv(
    const QGraphicsView *self) {
  return self->transformationAnchor();
}

//  void QGraphicsView::setTransformationAnchor(ViewportAnchor anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView23setTransformationAnchorENS_14ViewportAnchorE(
    QGraphicsView *self,
    QGraphicsView::ViewportAnchor anchor) {
  self->setTransformationAnchor(anchor);
}

//  ViewportAnchor QGraphicsView::resizeAnchor() const
extern "C" Q_DECL_EXPORT
QGraphicsView::ViewportAnchor ritual_ZNK13QGraphicsView12resizeAnchorEv(
    const QGraphicsView *self) {
  return self->resizeAnchor();
}

//  void QGraphicsView::setResizeAnchor(ViewportAnchor anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView15setResizeAnchorENS_14ViewportAnchorE(
    QGraphicsView *self,
    QGraphicsView::ViewportAnchor anchor) {
  self->setResizeAnchor(anchor);
}

//  ViewportUpdateMode QGraphicsView::viewportUpdateMode() const
extern "C" Q_DECL_EXPORT
QGraphicsView::ViewportUpdateMode ritual_ZNK13QGraphicsView18viewportUpdateModeEv(
    const QGraphicsView *self) {
  return self->viewportUpdateMode();
}

//  void QGraphicsView::setViewportUpdateMode(ViewportUpdateMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView21setViewportUpdateModeENS_18ViewportUpdateModeE(
    QGraphicsView *self,
    QGraphicsView::ViewportUpdateMode mode) {
  self->setViewportUpdateMode(mode);
}

//  OptimizationFlags QGraphicsView::optimizationFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsView17optimizationFlagsEv(
    const QGraphicsView *self) {
  return static_cast<int>(self->optimizationFlags().toInt());
}

//  void QGraphicsView::setOptimizationFlag(OptimizationFlag flag, bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView19setOptimizationFlagENS_16OptimizationFlagEb(
    QGraphicsView *self,
    QGraphicsView::OptimizationFlag flag,
    bool enabled) {
  self->setOptimizationFlag(flag, enabled);
}

//  void QGraphicsView::setOptimizationFlags(OptimizationFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView20setOptimizationFlagsE6QFlagsINS_16OptimizationFlagEE(
    QGraphicsView *self,
    int flags) {
  self->setOptimizationFlags(
      QFlags<QGraphicsView::OptimizationFlag>::fromInt(flags));
}

//  DragMode QGraphicsView::dragMode() const
extern "C" Q_DECL_EXPORT
QGraphicsView::DragMode ritual_ZNK13QGraphicsView8dragModeEv(
    const QGraphicsView *self) {
  return self->dragMode();
}

//  void QGraphicsView::setDragMode(DragMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView11setDragModeENS_8DragModeE(
    QGraphicsView *self,
    QGraphicsView::DragMode mode) {
  self->setDragMode(mode);
}

//  Qt::ItemSelectionMode QGraphicsView::rubberBandSelectionMode() const
extern "C" Q_DECL_EXPORT
Qt::ItemSelectionMode ritual_ZNK13QGraphicsView23rubberBandSelectionModeEv(
    const QGraphicsView *self) {
  return self->rubberBandSelectionMode();
}

//  void QGraphicsView::setRubberBandSelectionMode(Qt::ItemSelectionMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView26setRubberBandSelectionModeEN2Qt17ItemSelectionModeE(
    QGraphicsView *self,
    Qt::ItemSelectionMode mode) {
  self->setRubberBandSelectionMode(mode);
}

//  QRect QGraphicsView::rubberBandRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QGraphicsView14rubberBandRectEv(
    const QGraphicsView *self) {
  return new QRect(self->rubberBandRect());
}

//  CacheMode QGraphicsView::cacheMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QGraphicsView9cacheModeEv(const QGraphicsView *self) {
  return static_cast<int>(self->cacheMode().toInt());
}

//  void QGraphicsView::setCacheMode(CacheMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setCacheModeE6QFlagsINS_13CacheModeFlagEE(
    QGraphicsView *self,
    int mode) {
  self->setCacheMode(QFlags<QGraphicsView::CacheModeFlag>::fromInt(mode));
}

//  void QGraphicsView::resetCachedContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView18resetCachedContentEv(QGraphicsView *self) {
  self->resetCachedContent();
}

//  bool QGraphicsView::isInteractive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsView13isInteractiveEv(const QGraphicsView *self) {
  return self->isInteractive();
}

//  void QGraphicsView::setInteractive(bool allowed)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView14setInteractiveEb(
    QGraphicsView *self,
    bool allowed) {
  self->setInteractive(allowed);
}

//  QGraphicsScene *QGraphicsView::scene() const
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZNK13QGraphicsView5sceneEv(
    const QGraphicsView *self) {
  return self->scene();
}

//  void QGraphicsView::setScene(QGraphicsScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView8setSceneEP14QGraphicsScene(
    QGraphicsView *self,
    QGraphicsScene *scene) {
  self->setScene(scene);
}

//  QRectF QGraphicsView::sceneRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QGraphicsView9sceneRectEv(const QGraphicsView *self) {
  return new QRectF(self->sceneRect());
}

//  void QGraphicsView::setSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setSceneRectERK6QRectF(
    QGraphicsView *self,
    const QRectF *rect) {
  self->setSceneRect(*rect);
}

//  void QGraphicsView::setSceneRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setSceneRectEdddd(
    QGraphicsView *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setSceneRect(x, y, w, h);
}

//  QTransform QGraphicsView::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK13QGraphicsView9transformEv(
    const QGraphicsView *self) {
  return new QTransform(self->transform());
}

//  QTransform QGraphicsView::viewportTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK13QGraphicsView17viewportTransformEv(
    const QGraphicsView *self) {
  return new QTransform(self->viewportTransform());
}

//  bool QGraphicsView::isTransformed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGraphicsView13isTransformedEv(const QGraphicsView *self) {
  return self->isTransformed();
}

//  void QGraphicsView::setTransform(const QTransform &matrix, bool combine)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView12setTransformERK10QTransformb(
    QGraphicsView *self,
    const QTransform *matrix,
    bool combine) {
  self->setTransform(*matrix, combine);
}

//  void QGraphicsView::resetTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView14resetTransformEv(QGraphicsView *self) {
  self->resetTransform();
}

//  void QGraphicsView::rotate(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView6rotateEd(QGraphicsView *self, qreal angle) {
  self->rotate(angle);
}

//  void QGraphicsView::scale(qreal sx, qreal sy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView5scaleEdd(
    QGraphicsView *self,
    qreal sx,
    qreal sy) {
  self->scale(sx, sy);
}

//  void QGraphicsView::shear(qreal sh, qreal sv)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView5shearEdd(
    QGraphicsView *self,
    qreal sh,
    qreal sv) {
  self->shear(sh, sv);
}

//  void QGraphicsView::translate(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView9translateEdd(
    QGraphicsView *self,
    qreal dx,
    qreal dy) {
  self->translate(dx, dy);
}

//  void QGraphicsView::centerOn(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView8centerOnERK7QPointF(
    QGraphicsView *self,
    const QPointF *pos) {
  self->centerOn(*pos);
}

//  void QGraphicsView::centerOn(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView8centerOnEdd(
    QGraphicsView *self,
    qreal x,
    qreal y) {
  self->centerOn(x, y);
}

//  void QGraphicsView::centerOn(const QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView8centerOnEPK13QGraphicsItem(
    QGraphicsView *self,
    const QGraphicsItem *item) {
  self->centerOn(item);
}

//  void QGraphicsView::ensureVisible(const QRectF &rect, int xmargin, int
//      ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView13ensureVisibleERK6QRectFii(
    QGraphicsView *self,
    const QRectF *rect,
    int xmargin,
    int ymargin) {
  self->ensureVisible(*rect, xmargin, ymargin);
}

//  void QGraphicsView::ensureVisible(qreal x, qreal y, qreal w, qreal h, int
//      xmargin, int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView13ensureVisibleEddddii(
    QGraphicsView *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    int xmargin,
    int ymargin) {
  self->ensureVisible(x, y, w, h, xmargin, ymargin);
}

//  void QGraphicsView::ensureVisible(const QGraphicsItem *item, int xmargin,
//      int ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView13ensureVisibleEPK13QGraphicsItemii(
    QGraphicsView *self,
    const QGraphicsItem *item,
    int xmargin,
    int ymargin) {
  self->ensureVisible(item, xmargin, ymargin);
}

//  void QGraphicsView::fitInView(const QRectF &rect, Qt::AspectRatioMode
//      aspectRadioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView9fitInViewERK6QRectFN2Qt15AspectRatioModeE(
    QGraphicsView *self,
    const QRectF *rect,
    Qt::AspectRatioMode aspectRadioMode) {
  self->fitInView(*rect, aspectRadioMode);
}

//  void QGraphicsView::fitInView(qreal x, qreal y, qreal w, qreal h,
//      Qt::AspectRatioMode aspectRadioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView9fitInViewEddddN2Qt15AspectRatioModeE(
    QGraphicsView *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    Qt::AspectRatioMode aspectRadioMode) {
  self->fitInView(x, y, w, h, aspectRadioMode);
}

//  void QGraphicsView::fitInView(const QGraphicsItem *item,
//      Qt::AspectRatioMode aspectRadioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView9fitInViewEPK13QGraphicsItemN2Qt15AspectRatioModeE(
    QGraphicsView *self,
    const QGraphicsItem *item,
    Qt::AspectRatioMode aspectRadioMode) {
  self->fitInView(item, aspectRadioMode);
}

//  void QGraphicsView::render(QPainter *painter, const QRectF &target, const
//      QRect &source, Qt::AspectRatioMode aspectRatioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView6renderEP8QPainterRK6QRectFRK5QRectN2Qt15AspectRatioModeE(
    QGraphicsView *self,
    QPainter *painter,
    const QRectF *target,
    const QRect *source,
    Qt::AspectRatioMode aspectRatioMode) {
  self->render(painter, *target, *source, aspectRatioMode);
}

//  QGraphicsItem *QGraphicsView::itemAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsView6itemAtERK6QPoint(
    const QGraphicsView *self,
    const QPoint *pos) {
  return self->itemAt(*pos);
}

//  QGraphicsItem *QGraphicsView::itemAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK13QGraphicsView6itemAtEii(
    const QGraphicsView *self,
    int x,
    int y) {
  return self->itemAt(x, y);
}

//  QPointF QGraphicsView::mapToScene(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsView10mapToSceneERK6QPoint(
    const QGraphicsView *self,
    const QPoint *point) {
  return new QPointF(self->mapToScene(*point));
}

//  QPolygonF QGraphicsView::mapToScene(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsView10mapToSceneERK5QRect(
    const QGraphicsView *self,
    const QRect *rect) {
  return new QPolygonF(self->mapToScene(*rect));
}

//  QPolygonF QGraphicsView::mapToScene(const QPolygon &polygon) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsView10mapToSceneERK8QPolygon(
    const QGraphicsView *self,
    const QPolygon *polygon) {
  return new QPolygonF(self->mapToScene(*polygon));
}

//  QPainterPath QGraphicsView::mapToScene(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsView10mapToSceneERK12QPainterPath(
    const QGraphicsView *self,
    const QPainterPath *path) {
  return new QPainterPath(self->mapToScene(*path));
}

//  QPoint QGraphicsView::mapFromScene(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK13QGraphicsView12mapFromSceneERK7QPointF(
    const QGraphicsView *self,
    const QPointF *point) {
  return new QPoint(self->mapFromScene(*point));
}

//  QPolygon QGraphicsView::mapFromScene(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK13QGraphicsView12mapFromSceneERK6QRectF(
    const QGraphicsView *self,
    const QRectF *rect) {
  return new QPolygon(self->mapFromScene(*rect));
}

//  QPolygon QGraphicsView::mapFromScene(const QPolygonF &polygon) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK13QGraphicsView12mapFromSceneERK9QPolygonF(
    const QGraphicsView *self,
    const QPolygonF *polygon) {
  return new QPolygon(self->mapFromScene(*polygon));
}

//  QPainterPath QGraphicsView::mapFromScene(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13QGraphicsView12mapFromSceneERK12QPainterPath(
    const QGraphicsView *self,
    const QPainterPath *path) {
  return new QPainterPath(self->mapFromScene(*path));
}

//  QPointF QGraphicsView::mapToScene(int x, int y) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGraphicsView10mapToSceneEii(
    const QGraphicsView *self,
    int x,
    int y) {
  return new QPointF(self->mapToScene(x, y));
}

//  QPolygonF QGraphicsView::mapToScene(int x, int y, int w, int h) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK13QGraphicsView10mapToSceneEiiii(
    const QGraphicsView *self,
    int x,
    int y,
    int w,
    int h) {
  return new QPolygonF(self->mapToScene(x, y, w, h));
}

//  QPoint QGraphicsView::mapFromScene(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK13QGraphicsView12mapFromSceneEdd(
    const QGraphicsView *self,
    qreal x,
    qreal y) {
  return new QPoint(self->mapFromScene(x, y));
}

//  QPolygon QGraphicsView::mapFromScene(qreal x, qreal y, qreal w, qreal h)
//      const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK13QGraphicsView12mapFromSceneEdddd(
    const QGraphicsView *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygon(self->mapFromScene(x, y, w, h));
}

//  QVariant QGraphicsView::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QGraphicsView16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsView *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}

//  QBrush QGraphicsView::backgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QGraphicsView15backgroundBrushEv(
    const QGraphicsView *self) {
  return new QBrush(self->backgroundBrush());
}

//  void QGraphicsView::setBackgroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView18setBackgroundBrushERK6QBrush(
    QGraphicsView *self,
    const QBrush *brush) {
  self->setBackgroundBrush(*brush);
}

//  QBrush QGraphicsView::foregroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QGraphicsView15foregroundBrushEv(
    const QGraphicsView *self) {
  return new QBrush(self->foregroundBrush());
}

//  void QGraphicsView::setForegroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView18setForegroundBrushERK6QBrush(
    QGraphicsView *self,
    const QBrush *brush) {
  self->setForegroundBrush(*brush);
}

//  void QGraphicsView::invalidateScene(const QRectF &rect,
//      QGraphicsScene::SceneLayers layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView15invalidateSceneERK6QRectF6QFlagsIN14QGraphicsScene10SceneLayerEE(
    QGraphicsView *self,
    const QRectF *rect,
    int layers) {
  self->invalidateScene(
      *rect,
      QFlags<QGraphicsScene::SceneLayer>::fromInt(layers));
}

//  void QGraphicsView::updateSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGraphicsView15updateSceneRectERK6QRectF(
    QGraphicsView *self,
    const QRectF *rect) {
  self->updateSceneRect(*rect);
}

//  a Python function taken by a CuteQGraphicsView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsView(
    QGraphicsView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsView *>(self)->take(key, call);
}

//  QSize QGraphicsView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QGraphicsView8sizeHintEv(const QGraphicsView *self) {
  return new QSize(self->QGraphicsView::sizeHint());
}

//  QVariant QGraphicsView::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK13QGraphicsView16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsView *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->QGraphicsView::inputMethodQuery(query));
}

//  void QGraphicsView::setupViewport(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView13setupViewportEP7QWidget(
    QGraphicsView *self,
    QWidget *widget) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::setupViewport(
      widget);
}

//  bool QGraphicsView::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QGraphicsView5eventEP6QEvent(
    QGraphicsView *self,
    QEvent *event) {
  return static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::event(
      event);
}

//  bool QGraphicsView::viewportEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QGraphicsView13viewportEventEP6QEvent(
    QGraphicsView *self,
    QEvent *event) {
  return static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::viewportEvent(
      event);
}

//  void QGraphicsView::contextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView16contextMenuEventEP17QContextMenuEvent(
    QGraphicsView *self,
    QContextMenuEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::contextMenuEvent(
      event);
}

//  void QGraphicsView::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView14dragEnterEventEP15QDragEnterEvent(
    QGraphicsView *self,
    QDragEnterEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::dragEnterEvent(
      event);
}

//  void QGraphicsView::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView14dragLeaveEventEP15QDragLeaveEvent(
    QGraphicsView *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::dragLeaveEvent(
      event);
}

//  void QGraphicsView::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView13dragMoveEventEP14QDragMoveEvent(
    QGraphicsView *self,
    QDragMoveEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::dragMoveEvent(
      event);
}

//  void QGraphicsView::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView9dropEventEP10QDropEvent(
    QGraphicsView *self,
    QDropEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::dropEvent(event);
}

//  void QGraphicsView::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView12focusInEventEP11QFocusEvent(
    QGraphicsView *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::focusInEvent(
      event);
}

//  bool QGraphicsView::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QGraphicsView18focusNextPrevChildEb(
    QGraphicsView *self,
    bool next) {
  return static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::focusNextPrevChild(
      next);
}

//  void QGraphicsView::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView13focusOutEventEP11QFocusEvent(
    QGraphicsView *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::focusOutEvent(
      event);
}

//  void QGraphicsView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView13keyPressEventEP9QKeyEvent(
    QGraphicsView *self,
    QKeyEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::keyPressEvent(
      event);
}

//  void QGraphicsView::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView15keyReleaseEventEP9QKeyEvent(
    QGraphicsView *self,
    QKeyEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::keyReleaseEvent(
      event);
}

//  void QGraphicsView::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView21mouseDoubleClickEventEP11QMouseEvent(
    QGraphicsView *self,
    QMouseEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::mouseDoubleClickEvent(
      event);
}

//  void QGraphicsView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView15mousePressEventEP11QMouseEvent(
    QGraphicsView *self,
    QMouseEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::mousePressEvent(
      event);
}

//  void QGraphicsView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView14mouseMoveEventEP11QMouseEvent(
    QGraphicsView *self,
    QMouseEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::mouseMoveEvent(
      event);
}

//  void QGraphicsView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView17mouseReleaseEventEP11QMouseEvent(
    QGraphicsView *self,
    QMouseEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::mouseReleaseEvent(
      event);
}

//  void QGraphicsView::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView10wheelEventEP11QWheelEvent(
    QGraphicsView *self,
    QWheelEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::wheelEvent(event);
}

//  void QGraphicsView::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView10paintEventEP11QPaintEvent(
    QGraphicsView *self,
    QPaintEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::paintEvent(event);
}

//  void QGraphicsView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView11resizeEventEP12QResizeEvent(
    QGraphicsView *self,
    QResizeEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::resizeEvent(
      event);
}

//  void QGraphicsView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView16scrollContentsByEii(
    QGraphicsView *self,
    int dx,
    int dy) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::scrollContentsBy(
      dx,
      dy);
}

//  void QGraphicsView::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView9showEventEP10QShowEvent(
    QGraphicsView *self,
    QShowEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::showEvent(event);
}

//  void QGraphicsView::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView16inputMethodEventEP17QInputMethodEvent(
    QGraphicsView *self,
    QInputMethodEvent *event) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::inputMethodEvent(
      event);
}

//  void QGraphicsView::drawBackground(QPainter *painter, const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView14drawBackgroundEP8QPainterRK6QRectF(
    QGraphicsView *self,
    QPainter *painter,
    const QRectF *rect) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::drawBackground(
      painter,
      *rect);
}

//  void QGraphicsView::drawForeground(QPainter *painter, const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGraphicsView14drawForegroundEP8QPainterRK6QRectF(
    QGraphicsView *self,
    QPainter *painter,
    const QRectF *rect) {
  static_cast<OwnQGraphicsView *>(self)->OwnQGraphicsView::drawForeground(
      painter,
      *rect);
}
