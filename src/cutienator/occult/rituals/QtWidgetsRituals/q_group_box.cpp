//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgroupbox.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
#include <QtWidgets/qgroupbox.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGroupBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGroupBox : QGroupBox {
  using QGroupBox::event;
  using QGroupBox::childEvent;
  using QGroupBox::resizeEvent;
  using QGroupBox::paintEvent;
  using QGroupBox::focusInEvent;
  using QGroupBox::changeEvent;
  using QGroupBox::mousePressEvent;
  using QGroupBox::mouseMoveEvent;
  using QGroupBox::mouseReleaseEvent;
  using QGroupBox::initStyleOption;
};

//  A QGroupBox that Python can take functions over in. Every QGroupBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(groupbox)
typedef const QSize * (*CuteQGroupBoxCall0)(const void *, int *);
#endif  // QT_CONFIG(groupbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(groupbox)
typedef bool (*CuteQGroupBoxCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall2)(const void *, QChildEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall3)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall4)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall5)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall6)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall7)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall8)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall9)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
typedef void (*CuteQGroupBoxCall10)(const void *, QStyleOptionGroupBox *, int *);
#endif  // QT_CONFIG(groupbox)
typedef int (*CuteQGroupBoxCall11)(const void *, int *);
typedef void (*CuteQGroupBoxCall12)(const void *, bool, int *);
typedef const QSize * (*CuteQGroupBoxCall13)(const void *, int *);
typedef int (*CuteQGroupBoxCall14)(const void *, int, int *);
typedef bool (*CuteQGroupBoxCall15)(const void *, int *);
typedef void * (*CuteQGroupBoxCall16)(const void *, int *);
typedef void (*CuteQGroupBoxCall17)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQGroupBoxCall18)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQGroupBoxCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGroupBoxCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGroupBoxCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGroupBoxCall22)(const void *, QEnterEvent *, int *);
typedef void (*CuteQGroupBoxCall23)(const void *, QEvent *, int *);
typedef void (*CuteQGroupBoxCall24)(const void *, QMoveEvent *, int *);
typedef void (*CuteQGroupBoxCall25)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQGroupBoxCall26)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQGroupBoxCall27)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQGroupBoxCall28)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQGroupBoxCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQGroupBoxCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQGroupBoxCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQGroupBoxCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQGroupBoxCall33)(const void *, QShowEvent *, int *);
typedef void (*CuteQGroupBoxCall34)(const void *, QHideEvent *, int *);
typedef int (*CuteQGroupBoxCall35)(const void *, int, int *);
typedef void (*CuteQGroupBoxCall36)(const void *, QPainter *, int *);
typedef void * (*CuteQGroupBoxCall37)(const void *, QPoint *, int *);
typedef void * (*CuteQGroupBoxCall38)(const void *, int *);
typedef void (*CuteQGroupBoxCall39)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQGroupBoxCall40)(const void *, int, int *);
typedef bool (*CuteQGroupBoxCall41)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGroupBoxCall42)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGroupBoxCall43)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGroupBoxCall44)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGroupBoxCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGroupBoxCall46)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGroupBox : public QGroupBox {
public:
  using QGroupBox::QGroupBox;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
#if QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZNK9QGroupBox15initStyleOptionEP20QStyleOptionGroupBox")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(groupbox)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[25] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
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
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[41] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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

#if QT_CONFIG(groupbox)
  //  QSize QGroupBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGroupBoxCall0 call = reinterpret_cast<CuteQGroupBoxCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGroupBox::minimumSizeHint();
  }
#endif  // QT_CONFIG(groupbox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(groupbox)
  //  bool QGroupBox::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGroupBoxCall1 call = reinterpret_cast<CuteQGroupBoxCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGroupBox::event(event);
  }
#endif  // QT_CONFIG(groupbox)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(groupbox)
  //  void QGroupBox::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGroupBoxCall2 call = reinterpret_cast<CuteQGroupBoxCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGroupBox::childEvent(event);
  }
#endif  // QT_CONFIG(groupbox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(groupbox)
  //  void QGroupBox::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGroupBoxCall3 call = reinterpret_cast<CuteQGroupBoxCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGroupBox::resizeEvent(event);
  }
#endif  // QT_CONFIG(groupbox)

#if QT_CONFIG(groupbox)
  //  void QGroupBox::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGroupBoxCall4 call = reinterpret_cast<CuteQGroupBoxCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGroupBox::paintEvent(event);
  }
#endif  // QT_CONFIG(groupbox)

#if QT_CONFIG(groupbox)
  //  void QGroupBox::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGroupBoxCall5 call = reinterpret_cast<CuteQGroupBoxCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGroupBox::focusInEvent(event);
  }
#endif  // QT_CONFIG(groupbox)

#if QT_CONFIG(groupbox)
  //  void QGroupBox::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGroupBoxCall6 call = reinterpret_cast<CuteQGroupBoxCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGroupBox::changeEvent(event);
  }
#endif  // QT_CONFIG(groupbox)

#if QT_CONFIG(groupbox)
  //  void QGroupBox::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGroupBoxCall7 call = reinterpret_cast<CuteQGroupBoxCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGroupBox::mousePressEvent(event);
  }
#endif  // QT_CONFIG(groupbox)

#if QT_CONFIG(groupbox)
  //  void QGroupBox::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGroupBoxCall8 call = reinterpret_cast<CuteQGroupBoxCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGroupBox::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(groupbox)

#if QT_CONFIG(groupbox)
  //  void QGroupBox::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGroupBoxCall9 call = reinterpret_cast<CuteQGroupBoxCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGroupBox::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(groupbox)

#if QT_CONFIG(groupbox)
  //  void QGroupBox::initStyleOption(QStyleOptionGroupBox *option) const
  void initStyleOption(QStyleOptionGroupBox *option) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGroupBoxCall10 call = reinterpret_cast<CuteQGroupBoxCall10>(taken[10]);
      call(this, option, &handled);
      if (handled) return;
    }
    QGroupBox::initStyleOption(option);
  }
#endif  // QT_CONFIG(groupbox)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGroupBoxCall11 call = reinterpret_cast<CuteQGroupBoxCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGroupBoxCall12 call = reinterpret_cast<CuteQGroupBoxCall12>(taken[12]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGroupBoxCall13 call = reinterpret_cast<CuteQGroupBoxCall13>(taken[13]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQGroupBoxCall14 call = reinterpret_cast<CuteQGroupBoxCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQGroupBoxCall15 call = reinterpret_cast<CuteQGroupBoxCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQGroupBoxCall16 call = reinterpret_cast<CuteQGroupBoxCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGroupBoxCall17 call = reinterpret_cast<CuteQGroupBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGroupBoxCall18 call = reinterpret_cast<CuteQGroupBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGroupBoxCall19 call = reinterpret_cast<CuteQGroupBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGroupBoxCall20 call = reinterpret_cast<CuteQGroupBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGroupBoxCall21 call = reinterpret_cast<CuteQGroupBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGroupBoxCall22 call = reinterpret_cast<CuteQGroupBoxCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGroupBoxCall23 call = reinterpret_cast<CuteQGroupBoxCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGroupBoxCall24 call = reinterpret_cast<CuteQGroupBoxCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGroupBoxCall25 call = reinterpret_cast<CuteQGroupBoxCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGroupBoxCall26 call = reinterpret_cast<CuteQGroupBoxCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGroupBoxCall27 call = reinterpret_cast<CuteQGroupBoxCall27>(taken[27]);
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
      CuteQGroupBoxCall28 call = reinterpret_cast<CuteQGroupBoxCall28>(taken[28]);
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
      CuteQGroupBoxCall29 call = reinterpret_cast<CuteQGroupBoxCall29>(taken[29]);
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
      CuteQGroupBoxCall30 call = reinterpret_cast<CuteQGroupBoxCall30>(taken[30]);
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
      CuteQGroupBoxCall31 call = reinterpret_cast<CuteQGroupBoxCall31>(taken[31]);
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
      CuteQGroupBoxCall32 call = reinterpret_cast<CuteQGroupBoxCall32>(taken[32]);
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
      CuteQGroupBoxCall33 call = reinterpret_cast<CuteQGroupBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQGroupBoxCall34 call = reinterpret_cast<CuteQGroupBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQGroupBoxCall35 call = reinterpret_cast<CuteQGroupBoxCall35>(taken[35]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQGroupBoxCall36 call = reinterpret_cast<CuteQGroupBoxCall36>(taken[36]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQGroupBoxCall37 call = reinterpret_cast<CuteQGroupBoxCall37>(taken[37]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQGroupBoxCall38 call = reinterpret_cast<CuteQGroupBoxCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQGroupBoxCall39 call = reinterpret_cast<CuteQGroupBoxCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQGroupBoxCall40 call = reinterpret_cast<CuteQGroupBoxCall40>(taken[40]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQGroupBoxCall41 call = reinterpret_cast<CuteQGroupBoxCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQGroupBoxCall42 call = reinterpret_cast<CuteQGroupBoxCall42>(taken[42]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQGroupBoxCall43 call = reinterpret_cast<CuteQGroupBoxCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQGroupBoxCall44 call = reinterpret_cast<CuteQGroupBoxCall44>(taken[44]);
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
      CuteQGroupBoxCall45 call = reinterpret_cast<CuteQGroupBoxCall45>(taken[45]);
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
      CuteQGroupBoxCall46 call = reinterpret_cast<CuteQGroupBoxCall46>(taken[46]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGroupBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QGroupBox10metaObjectEv(
    const QGroupBox *self) {
  return self->metaObject();
}

//  QString QGroupBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QGroupBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGroupBox::tr(s, c, n));
}

//  QGroupBox::QGroupBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QGroupBox *ritual_ZN9QGroupBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQGroupBox(parent);
}

//  QGroupBox::QGroupBox(const QString &title, QWidget *parent)
extern "C" Q_DECL_EXPORT
QGroupBox *ritual_ZN9QGroupBoxC1ERK7QStringP7QWidget(
    const QString *title,
    QWidget *parent) {
  return new CuteQGroupBox(*title, parent);
}

//  QGroupBox::~QGroupBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBoxD1Ev(QGroupBox *self) {
  delete self;
}

//  QString QGroupBox::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QGroupBox5titleEv(const QGroupBox *self) {
  return new QString(self->title());
}

//  void QGroupBox::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox8setTitleERK7QString(
    QGroupBox *self,
    const QString *title) {
  self->setTitle(*title);
}

//  Qt::Alignment QGroupBox::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QGroupBox9alignmentEv(const QGroupBox *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QGroupBox::setAlignment(int alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox12setAlignmentEi(QGroupBox *self, int alignment) {
  self->setAlignment(alignment);
}

//  QSize QGroupBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QGroupBox15minimumSizeHintEv(const QGroupBox *self) {
  return new QSize(self->minimumSizeHint());
}

//  bool QGroupBox::isFlat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGroupBox6isFlatEv(const QGroupBox *self) {
  return self->isFlat();
}

//  void QGroupBox::setFlat(bool flat)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox7setFlatEb(QGroupBox *self, bool flat) {
  self->setFlat(flat);
}

//  bool QGroupBox::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGroupBox11isCheckableEv(const QGroupBox *self) {
  return self->isCheckable();
}

//  void QGroupBox::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox12setCheckableEb(QGroupBox *self, bool checkable) {
  self->setCheckable(checkable);
}

//  bool QGroupBox::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGroupBox9isCheckedEv(const QGroupBox *self) {
  return self->isChecked();
}

//  void QGroupBox::setChecked(bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox10setCheckedEb(QGroupBox *self, bool checked) {
  self->setChecked(checked);
}

//  bool QGroupBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QGroupBox5eventEP6QEvent(QGroupBox *self, QEvent *event) {
  return self->event(event);
}

//  void QGroupBox::childEvent(QChildEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox10childEventEP11QChildEvent(
    QGroupBox *self,
    QChildEvent *event) {
  self->childEvent(event);
}

//  void QGroupBox::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox11resizeEventEP12QResizeEvent(
    QGroupBox *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QGroupBox::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox10paintEventEP11QPaintEvent(
    QGroupBox *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QGroupBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox12focusInEventEP11QFocusEvent(
    QGroupBox *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QGroupBox::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox11changeEventEP6QEvent(
    QGroupBox *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  void QGroupBox::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox15mousePressEventEP11QMouseEvent(
    QGroupBox *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QGroupBox::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox14mouseMoveEventEP11QMouseEvent(
    QGroupBox *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QGroupBox::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGroupBox17mouseReleaseEventEP11QMouseEvent(
    QGroupBox *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QGroupBox::initStyleOption(QStyleOptionGroupBox *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QGroupBox15initStyleOptionEP20QStyleOptionGroupBox(
    const QGroupBox *self,
    QStyleOptionGroupBox *option) {
  self->initStyleOption(option);
}

//  a Python function taken by a CuteQGroupBox, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGroupBox(QGroupBox *self, const char *key, void *call) {
  return static_cast<CuteQGroupBox *>(self)->take(key, call);
}

//  QSize QGroupBox::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QGroupBox15minimumSizeHintEv(const QGroupBox *self) {
  return new QSize(self->QGroupBox::minimumSizeHint());
}

//  bool QGroupBox::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QGroupBox5eventEP6QEvent(QGroupBox *self, QEvent *event) {
  return static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::event(event);
}

//  void QGroupBox::childEvent(QChildEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QGroupBox10childEventEP11QChildEvent(
    QGroupBox *self,
    QChildEvent *event) {
  static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::childEvent(event);
}

//  void QGroupBox::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QGroupBox11resizeEventEP12QResizeEvent(
    QGroupBox *self,
    QResizeEvent *event) {
  static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::resizeEvent(event);
}

//  void QGroupBox::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QGroupBox10paintEventEP11QPaintEvent(
    QGroupBox *self,
    QPaintEvent *event) {
  static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::paintEvent(event);
}

//  void QGroupBox::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QGroupBox12focusInEventEP11QFocusEvent(
    QGroupBox *self,
    QFocusEvent *event) {
  static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::focusInEvent(event);
}

//  void QGroupBox::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QGroupBox11changeEventEP6QEvent(
    QGroupBox *self,
    QEvent *event) {
  static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::changeEvent(event);
}

//  void QGroupBox::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QGroupBox15mousePressEventEP11QMouseEvent(
    QGroupBox *self,
    QMouseEvent *event) {
  static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::mousePressEvent(event);
}

//  void QGroupBox::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QGroupBox14mouseMoveEventEP11QMouseEvent(
    QGroupBox *self,
    QMouseEvent *event) {
  static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::mouseMoveEvent(event);
}

//  void QGroupBox::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QGroupBox17mouseReleaseEventEP11QMouseEvent(
    QGroupBox *self,
    QMouseEvent *event) {
  static_cast<OwnQGroupBox *>(self)->OwnQGroupBox::mouseReleaseEvent(event);
}

//  void QGroupBox::initStyleOption(QStyleOptionGroupBox *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9QGroupBox15initStyleOptionEP20QStyleOptionGroupBox(
    const QGroupBox *self,
    QStyleOptionGroupBox *option) {
  static_cast<const OwnQGroupBox *>(self)->OwnQGroupBox::initStyleOption(
      option);
}

#endif  // QT_CONFIG(groupbox)
#endif  // QT_CONFIG(groupbox)
