//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlabel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(label)
#if QT_CONFIG(label)
#include <QtWidgets/qlabel.h>
#include <QtCore/qstring.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpicture.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLabel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLabel : QLabel {
  using QLabel::event;
  using QLabel::keyPressEvent;
  using QLabel::paintEvent;
  using QLabel::changeEvent;
  using QLabel::mousePressEvent;
  using QLabel::mouseMoveEvent;
  using QLabel::mouseReleaseEvent;
  using QLabel::contextMenuEvent;
  using QLabel::focusInEvent;
  using QLabel::focusOutEvent;
  using QLabel::focusNextPrevChild;
};

//  A QLabel that Python can take functions over in. Every QLabel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(label)
typedef const QSize * (*CuteQLabelCall0)(const void *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef const QSize * (*CuteQLabelCall1)(const void *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef int (*CuteQLabelCall2)(const void *, int, int *);
#endif  // QT_CONFIG(label)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(label)
typedef bool (*CuteQLabelCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(label)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall4)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall5)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall6)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall7)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall8)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall9)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(label)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall10)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(label)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall11)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef void (*CuteQLabelCall12)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
typedef bool (*CuteQLabelCall13)(const void *, bool, int *);
#endif  // QT_CONFIG(label)
typedef void (*CuteQLabelCall14)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQLabelCall15)(const void *, int *);
typedef void (*CuteQLabelCall16)(const void *, bool, int *);
typedef bool (*CuteQLabelCall17)(const void *, int *);
typedef void * (*CuteQLabelCall18)(const void *, int *);
typedef void (*CuteQLabelCall19)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQLabelCall20)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQLabelCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQLabelCall22)(const void *, QEnterEvent *, int *);
typedef void (*CuteQLabelCall23)(const void *, QEvent *, int *);
typedef void (*CuteQLabelCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQLabelCall25)(const void *, QResizeEvent *, int *);
typedef void (*CuteQLabelCall26)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQLabelCall27)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQLabelCall28)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQLabelCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQLabelCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQLabelCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQLabelCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQLabelCall33)(const void *, QShowEvent *, int *);
typedef void (*CuteQLabelCall34)(const void *, QHideEvent *, int *);
typedef int (*CuteQLabelCall35)(const void *, int, int *);
typedef void (*CuteQLabelCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQLabelCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQLabelCall38)(const void *, int *);
typedef void (*CuteQLabelCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQLabelCall40)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLabelCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLabelCall42)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLabelCall43)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLabelCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLabelCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLabelCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLabel : public QLabel {
public:
  using QLabel::QLabel;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
#if QT_CONFIG(label)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(label)
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(label)
  //  QSize QLabel::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLabelCall0 call = reinterpret_cast<CuteQLabelCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLabel::sizeHint();
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  QSize QLabel::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLabelCall1 call = reinterpret_cast<CuteQLabelCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLabel::minimumSizeHint();
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  int QLabel::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLabelCall2 call = reinterpret_cast<CuteQLabelCall2>(taken[2]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLabel::heightForWidth(a0);
  }
#endif  // QT_CONFIG(label)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(label)
  //  bool QLabel::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLabelCall3 call = reinterpret_cast<CuteQLabelCall3>(taken[3]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QLabel::event(e);
  }
#endif  // QT_CONFIG(label)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(label)
  //  void QLabel::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLabelCall4 call = reinterpret_cast<CuteQLabelCall4>(taken[4]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QLabel::keyPressEvent(ev);
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  void QLabel::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLabelCall5 call = reinterpret_cast<CuteQLabelCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLabel::paintEvent(a0);
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  void QLabel::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLabelCall6 call = reinterpret_cast<CuteQLabelCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLabel::changeEvent(a0);
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  void QLabel::mousePressEvent(QMouseEvent *ev)
  void mousePressEvent(QMouseEvent *ev) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLabelCall7 call = reinterpret_cast<CuteQLabelCall7>(taken[7]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QLabel::mousePressEvent(ev);
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  void QLabel::mouseMoveEvent(QMouseEvent *ev)
  void mouseMoveEvent(QMouseEvent *ev) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLabelCall8 call = reinterpret_cast<CuteQLabelCall8>(taken[8]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QLabel::mouseMoveEvent(ev);
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  void QLabel::mouseReleaseEvent(QMouseEvent *ev)
  void mouseReleaseEvent(QMouseEvent *ev) override {
    if (taken[9]) {
      int handled = 0;
      CuteQLabelCall9 call = reinterpret_cast<CuteQLabelCall9>(taken[9]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QLabel::mouseReleaseEvent(ev);
  }
#endif  // QT_CONFIG(label)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(label)
  //  void QLabel::contextMenuEvent(QContextMenuEvent *ev)
  void contextMenuEvent(QContextMenuEvent *ev) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLabelCall10 call = reinterpret_cast<CuteQLabelCall10>(taken[10]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QLabel::contextMenuEvent(ev);
  }
#endif  // QT_CONFIG(label)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(label)
  //  void QLabel::focusInEvent(QFocusEvent *ev)
  void focusInEvent(QFocusEvent *ev) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLabelCall11 call = reinterpret_cast<CuteQLabelCall11>(taken[11]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QLabel::focusInEvent(ev);
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  void QLabel::focusOutEvent(QFocusEvent *ev)
  void focusOutEvent(QFocusEvent *ev) override {
    if (taken[12]) {
      int handled = 0;
      CuteQLabelCall12 call = reinterpret_cast<CuteQLabelCall12>(taken[12]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QLabel::focusOutEvent(ev);
  }
#endif  // QT_CONFIG(label)

#if QT_CONFIG(label)
  //  bool QLabel::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[13]) {
      int handled = 0;
      CuteQLabelCall13 call = reinterpret_cast<CuteQLabelCall13>(taken[13]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QLabel::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(label)

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQLabelCall14 call = reinterpret_cast<CuteQLabelCall14>(taken[14]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQLabelCall15 call = reinterpret_cast<CuteQLabelCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLabelCall16 call = reinterpret_cast<CuteQLabelCall16>(taken[16]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQLabelCall17 call = reinterpret_cast<CuteQLabelCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQLabelCall18 call = reinterpret_cast<CuteQLabelCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQLabelCall19 call = reinterpret_cast<CuteQLabelCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLabelCall20 call = reinterpret_cast<CuteQLabelCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQLabelCall21 call = reinterpret_cast<CuteQLabelCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQLabelCall22 call = reinterpret_cast<CuteQLabelCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQLabelCall23 call = reinterpret_cast<CuteQLabelCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQLabelCall24 call = reinterpret_cast<CuteQLabelCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQLabelCall25 call = reinterpret_cast<CuteQLabelCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQLabelCall26 call = reinterpret_cast<CuteQLabelCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQLabelCall27 call = reinterpret_cast<CuteQLabelCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQLabelCall28 call = reinterpret_cast<CuteQLabelCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQLabelCall29 call = reinterpret_cast<CuteQLabelCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQLabelCall30 call = reinterpret_cast<CuteQLabelCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQLabelCall31 call = reinterpret_cast<CuteQLabelCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQLabelCall32 call = reinterpret_cast<CuteQLabelCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQLabelCall33 call = reinterpret_cast<CuteQLabelCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQLabelCall34 call = reinterpret_cast<CuteQLabelCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQLabelCall35 call = reinterpret_cast<CuteQLabelCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQLabelCall36 call = reinterpret_cast<CuteQLabelCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQLabelCall37 call = reinterpret_cast<CuteQLabelCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQLabelCall38 call = reinterpret_cast<CuteQLabelCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQLabelCall39 call = reinterpret_cast<CuteQLabelCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQLabelCall40 call = reinterpret_cast<CuteQLabelCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQLabelCall41 call = reinterpret_cast<CuteQLabelCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQLabelCall42 call = reinterpret_cast<CuteQLabelCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQLabelCall43 call = reinterpret_cast<CuteQLabelCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQLabelCall44 call = reinterpret_cast<CuteQLabelCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQLabelCall45 call = reinterpret_cast<CuteQLabelCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[46]) {
      int handled = 0;
      CuteQLabelCall46 call = reinterpret_cast<CuteQLabelCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QLabel10metaObjectEv(const QLabel *self) {
  return self->metaObject();
}

//  QString QLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QLabel2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QLabel::tr(s, c, n));
}

//  QLabel::QLabel(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QLabel *ritual_ZN6QLabelC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQLabel(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QLabel::QLabel(const QString &text, QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QLabel *ritual_ZN6QLabelC1ERK7QStringP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *text,
    QWidget *parent,
    int f) {
  return new CuteQLabel(*text, parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QLabel::~QLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabelD1Ev(QLabel *self) {
  delete self;
}

//  QString QLabel::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QLabel4textEv(const QLabel *self) {
  return new QString(self->text());
}

#if QT_DEPRECATED_SINCE(6,6)
//  QPixmap QLabel::pixmap(Qt::ReturnByValueConstant a0) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK6QLabel6pixmapEN2Qt21ReturnByValueConstantE(
    const QLabel *self,
    Qt::ReturnByValueConstant a0) {
  return new QPixmap(self->pixmap(a0));
}
#endif  // QT_DEPRECATED_SINCE(6,6)

//  QPixmap QLabel::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK6QLabel6pixmapEv(const QLabel *self) {
  return new QPixmap(self->pixmap());
}

#if !defined(QT_NO_PICTURE)
#if QT_DEPRECATED_SINCE(6,6)
//  QPicture QLabel::picture(Qt::ReturnByValueConstant a0) const
extern "C" Q_DECL_EXPORT
QPicture *ritual_ZNK6QLabel7pictureEN2Qt21ReturnByValueConstantE(
    const QLabel *self,
    Qt::ReturnByValueConstant a0) {
  return new QPicture(self->picture(a0));
}
#endif  // QT_DEPRECATED_SINCE(6,6)
#endif  // !defined(QT_NO_PICTURE)

#if !defined(QT_NO_PICTURE)
//  QPicture QLabel::picture() const
extern "C" Q_DECL_EXPORT
QPicture *ritual_ZNK6QLabel7pictureEv(const QLabel *self) {
  return new QPicture(self->picture());
}
#endif  // !defined(QT_NO_PICTURE)

#if QT_CONFIG(movie)
//  QMovie *QLabel::movie() const
extern "C" Q_DECL_EXPORT
QMovie *ritual_ZNK6QLabel5movieEv(const QLabel *self) {
  return self->movie();
}
#endif  // QT_CONFIG(movie)

//  Qt::TextFormat QLabel::textFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK6QLabel10textFormatEv(const QLabel *self) {
  return self->textFormat();
}

//  void QLabel::setTextFormat(Qt::TextFormat a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel13setTextFormatEN2Qt10TextFormatE(
    QLabel *self,
    Qt::TextFormat a0) {
  self->setTextFormat(a0);
}

//  Qt::Alignment QLabel::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel9alignmentEv(const QLabel *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QLabel::setAlignment(Qt::Alignment a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QLabel *self,
    int a0) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(a0));
}

//  void QLabel::setWordWrap(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel11setWordWrapEb(QLabel *self, bool on) {
  self->setWordWrap(on);
}

//  bool QLabel::wordWrap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLabel8wordWrapEv(const QLabel *self) {
  return self->wordWrap();
}

//  int QLabel::indent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel6indentEv(const QLabel *self) {
  return self->indent();
}

//  void QLabel::setIndent(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel9setIndentEi(QLabel *self, int a0) {
  self->setIndent(a0);
}

//  int QLabel::margin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel6marginEv(const QLabel *self) {
  return self->margin();
}

//  void QLabel::setMargin(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel9setMarginEi(QLabel *self, int a0) {
  self->setMargin(a0);
}

//  bool QLabel::hasScaledContents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLabel17hasScaledContentsEv(const QLabel *self) {
  return self->hasScaledContents();
}

//  void QLabel::setScaledContents(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel17setScaledContentsEb(QLabel *self, bool a0) {
  self->setScaledContents(a0);
}

//  QSize QLabel::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QLabel8sizeHintEv(const QLabel *self) {
  return new QSize(self->sizeHint());
}

//  QSize QLabel::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QLabel15minimumSizeHintEv(const QLabel *self) {
  return new QSize(self->minimumSizeHint());
}

#if !defined(QT_NO_SHORTCUT)
//  void QLabel::setBuddy(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel8setBuddyEP7QWidget(QLabel *self, QWidget *a0) {
  self->setBuddy(a0);
}
#endif  // !defined(QT_NO_SHORTCUT)

#if !defined(QT_NO_SHORTCUT)
//  QWidget *QLabel::buddy() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK6QLabel5buddyEv(const QLabel *self) {
  return self->buddy();
}
#endif  // !defined(QT_NO_SHORTCUT)

//  int QLabel::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel14heightForWidthEi(const QLabel *self, int a0) {
  return self->heightForWidth(a0);
}

//  bool QLabel::openExternalLinks() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLabel17openExternalLinksEv(const QLabel *self) {
  return self->openExternalLinks();
}

//  void QLabel::setOpenExternalLinks(bool open)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel20setOpenExternalLinksEb(QLabel *self, bool open) {
  self->setOpenExternalLinks(open);
}

//  void QLabel::setTextInteractionFlags(Qt::TextInteractionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QLabel *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QLabel::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel20textInteractionFlagsEv(const QLabel *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QLabel::setSelection(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel12setSelectionEii(QLabel *self, int a0, int a1) {
  self->setSelection(a0, a1);
}

//  bool QLabel::hasSelectedText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLabel15hasSelectedTextEv(const QLabel *self) {
  return self->hasSelectedText();
}

//  QString QLabel::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QLabel12selectedTextEv(const QLabel *self) {
  return new QString(self->selectedText());
}

//  int QLabel::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLabel14selectionStartEv(const QLabel *self) {
  return self->selectionStart();
}

//  void QLabel::setText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel7setTextERK7QString(QLabel *self, const QString *a0) {
  self->setText(*a0);
}

//  void QLabel::setPixmap(const QPixmap &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel9setPixmapERK7QPixmap(QLabel *self, const QPixmap *a0) {
  self->setPixmap(*a0);
}

#if !defined(QT_NO_PICTURE)
//  void QLabel::setPicture(const QPicture &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel10setPictureERK8QPicture(
    QLabel *self,
    const QPicture *a0) {
  self->setPicture(*a0);
}
#endif  // !defined(QT_NO_PICTURE)

#if QT_CONFIG(movie)
//  void QLabel::setMovie(QMovie *movie)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel8setMovieEP6QMovie(QLabel *self, QMovie *movie) {
  self->setMovie(movie);
}
#endif  // QT_CONFIG(movie)

//  void QLabel::setNum(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel6setNumEi(QLabel *self, int a0) {
  self->setNum(a0);
}

//  void QLabel::setNum(double a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel6setNumEd(QLabel *self, double a0) {
  self->setNum(a0);
}

//  void QLabel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel5clearEv(QLabel *self) {
  self->clear();
}

//  bool QLabel::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QLabel5eventEP6QEvent(QLabel *self, QEvent *e) {
  return self->event(e);
}

//  void QLabel::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel13keyPressEventEP9QKeyEvent(
    QLabel *self,
    QKeyEvent *ev) {
  self->keyPressEvent(ev);
}

//  void QLabel::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel10paintEventEP11QPaintEvent(
    QLabel *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QLabel::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel11changeEventEP6QEvent(QLabel *self, QEvent *a0) {
  self->changeEvent(a0);
}

//  void QLabel::mousePressEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel15mousePressEventEP11QMouseEvent(
    QLabel *self,
    QMouseEvent *ev) {
  self->mousePressEvent(ev);
}

//  void QLabel::mouseMoveEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel14mouseMoveEventEP11QMouseEvent(
    QLabel *self,
    QMouseEvent *ev) {
  self->mouseMoveEvent(ev);
}

//  void QLabel::mouseReleaseEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel17mouseReleaseEventEP11QMouseEvent(
    QLabel *self,
    QMouseEvent *ev) {
  self->mouseReleaseEvent(ev);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QLabel::contextMenuEvent(QContextMenuEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel16contextMenuEventEP17QContextMenuEvent(
    QLabel *self,
    QContextMenuEvent *ev) {
  self->contextMenuEvent(ev);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  void QLabel::focusInEvent(QFocusEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel12focusInEventEP11QFocusEvent(
    QLabel *self,
    QFocusEvent *ev) {
  self->focusInEvent(ev);
}

//  void QLabel::focusOutEvent(QFocusEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLabel13focusOutEventEP11QFocusEvent(
    QLabel *self,
    QFocusEvent *ev) {
  self->focusOutEvent(ev);
}

//  bool QLabel::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QLabel18focusNextPrevChildEb(QLabel *self, bool next) {
  return self->focusNextPrevChild(next);
}

//  QLabelPrivate *QLabel::d_func()
extern "C" Q_DECL_EXPORT
QLabelPrivate *ritual_ZN6QLabel6d_funcEv(QLabel *self) {
  return self->d_func();
}

//  const QLabelPrivate *QLabel::d_func() const
extern "C" Q_DECL_EXPORT
const QLabelPrivate *ritual_ZNK6QLabel6d_funcEv(const QLabel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQLabel, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLabel(QLabel *self, const char *key, void *call) {
  return static_cast<CuteQLabel *>(self)->take(key, call);
}

//  QSize QLabel::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK6QLabel8sizeHintEv(const QLabel *self) {
  return new QSize(self->QLabel::sizeHint());
}

//  QSize QLabel::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK6QLabel15minimumSizeHintEv(const QLabel *self) {
  return new QSize(self->QLabel::minimumSizeHint());
}

//  int QLabel::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK6QLabel14heightForWidthEi(const QLabel *self, int a0) {
  return self->QLabel::heightForWidth(a0);
}

//  bool QLabel::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QLabel5eventEP6QEvent(QLabel *self, QEvent *e) {
  return static_cast<OwnQLabel *>(self)->OwnQLabel::event(e);
}

//  void QLabel::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel13keyPressEventEP9QKeyEvent(
    QLabel *self,
    QKeyEvent *ev) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::keyPressEvent(ev);
}

//  void QLabel::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel10paintEventEP11QPaintEvent(
    QLabel *self,
    QPaintEvent *a0) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::paintEvent(a0);
}

//  void QLabel::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel11changeEventEP6QEvent(QLabel *self, QEvent *a0) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::changeEvent(a0);
}

//  void QLabel::mousePressEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel15mousePressEventEP11QMouseEvent(
    QLabel *self,
    QMouseEvent *ev) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::mousePressEvent(ev);
}

//  void QLabel::mouseMoveEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel14mouseMoveEventEP11QMouseEvent(
    QLabel *self,
    QMouseEvent *ev) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::mouseMoveEvent(ev);
}

//  void QLabel::mouseReleaseEvent(QMouseEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel17mouseReleaseEventEP11QMouseEvent(
    QLabel *self,
    QMouseEvent *ev) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::mouseReleaseEvent(ev);
}

#if !defined(QT_NO_CONTEXTMENU)
//  void QLabel::contextMenuEvent(QContextMenuEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel16contextMenuEventEP17QContextMenuEvent(
    QLabel *self,
    QContextMenuEvent *ev) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::contextMenuEvent(ev);
}
#endif  // !defined(QT_NO_CONTEXTMENU)

//  void QLabel::focusInEvent(QFocusEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel12focusInEventEP11QFocusEvent(
    QLabel *self,
    QFocusEvent *ev) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::focusInEvent(ev);
}

//  void QLabel::focusOutEvent(QFocusEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QLabel13focusOutEventEP11QFocusEvent(
    QLabel *self,
    QFocusEvent *ev) {
  static_cast<OwnQLabel *>(self)->OwnQLabel::focusOutEvent(ev);
}

//  bool QLabel::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QLabel18focusNextPrevChildEb(QLabel *self, bool next) {
  return static_cast<OwnQLabel *>(self)->OwnQLabel::focusNextPrevChild(next);
}

#endif  // QT_CONFIG(label)
#endif  // QT_CONFIG(label)
