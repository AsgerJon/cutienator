//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtabbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(tabbar)
#include <QtWidgets/qtabbar.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QTabBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTabBar : QTabBar {
  using QTabBar::tabSizeHint;
  using QTabBar::minimumTabSizeHint;
  using QTabBar::tabInserted;
  using QTabBar::tabRemoved;
  using QTabBar::tabLayoutChange;
  using QTabBar::event;
  using QTabBar::resizeEvent;
  using QTabBar::showEvent;
  using QTabBar::hideEvent;
  using QTabBar::paintEvent;
  using QTabBar::mousePressEvent;
  using QTabBar::mouseMoveEvent;
  using QTabBar::mouseReleaseEvent;
  using QTabBar::mouseDoubleClickEvent;
  using QTabBar::wheelEvent;
  using QTabBar::keyPressEvent;
  using QTabBar::changeEvent;
  using QTabBar::timerEvent;
  using QTabBar::initStyleOption;
};

//  A QTabBar that Python can take functions over in. Every QTabBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(tabbar)
typedef const QSize * (*CuteQTabBarCall0)(const void *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef const QSize * (*CuteQTabBarCall1)(const void *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef const QSize * (*CuteQTabBarCall2)(const void *, int, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef const QSize * (*CuteQTabBarCall3)(const void *, int, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall4)(const void *, int, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall5)(const void *, int, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall6)(const void *, int *);
#endif  // QT_CONFIG(tabbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
typedef bool (*CuteQTabBarCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall8)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall9)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall10)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall11)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall12)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall13)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall14)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall15)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall16)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall17)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall18)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall19)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
typedef void (*CuteQTabBarCall20)(const void *, QStyleOptionTab *, int, int *);
#endif  // QT_CONFIG(tabbar)
typedef int (*CuteQTabBarCall21)(const void *, int *);
typedef void (*CuteQTabBarCall22)(const void *, bool, int *);
typedef int (*CuteQTabBarCall23)(const void *, int, int *);
typedef bool (*CuteQTabBarCall24)(const void *, int *);
typedef void * (*CuteQTabBarCall25)(const void *, int *);
typedef void (*CuteQTabBarCall26)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTabBarCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQTabBarCall28)(const void *, QFocusEvent *, int *);
typedef void (*CuteQTabBarCall29)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTabBarCall30)(const void *, QEvent *, int *);
typedef void (*CuteQTabBarCall31)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTabBarCall32)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQTabBarCall33)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQTabBarCall34)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQTabBarCall35)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQTabBarCall36)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQTabBarCall37)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQTabBarCall38)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQTabBarCall39)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef int (*CuteQTabBarCall40)(const void *, int, int *);
typedef void (*CuteQTabBarCall41)(const void *, QPainter *, int *);
typedef void * (*CuteQTabBarCall42)(const void *, QPoint *, int *);
typedef void * (*CuteQTabBarCall43)(const void *, int *);
typedef void (*CuteQTabBarCall44)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQTabBarCall45)(const void *, int, int *);
typedef bool (*CuteQTabBarCall46)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTabBarCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabBarCall48)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabBarCall49)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabBarCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTabBarCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTabBar : public QTabBar {
public:
  using QTabBar::QTabBar;
  void *taken[52] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK7QTabBar11tabSizeHintEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK7QTabBar18minimumTabSizeHintEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QTabBar11tabInsertedEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QTabBar10tabRemovedEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QTabBar15tabLayoutChangeEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK7QTabBar15initStyleOptionEP15QStyleOptionTabi")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[32] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
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
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[46] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(tabbar)
  //  QSize QTabBar::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTabBarCall0 call = reinterpret_cast<CuteQTabBarCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTabBar::sizeHint();
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  QSize QTabBar::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTabBarCall1 call = reinterpret_cast<CuteQTabBarCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTabBar::minimumSizeHint();
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  QSize QTabBar::tabSizeHint(int index) const
  QSize tabSizeHint(int index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTabBarCall2 call = reinterpret_cast<CuteQTabBarCall2>(taken[2]);
      const QSize * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return QTabBar::tabSizeHint(index);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  QSize QTabBar::minimumTabSizeHint(int index) const
  QSize minimumTabSizeHint(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTabBarCall3 call = reinterpret_cast<CuteQTabBarCall3>(taken[3]);
      const QSize * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return QTabBar::minimumTabSizeHint(index);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::tabInserted(int index)
  void tabInserted(int index) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTabBarCall4 call = reinterpret_cast<CuteQTabBarCall4>(taken[4]);
      call(this, index, &handled);
      if (handled) return;
    }
    QTabBar::tabInserted(index);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::tabRemoved(int index)
  void tabRemoved(int index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTabBarCall5 call = reinterpret_cast<CuteQTabBarCall5>(taken[5]);
      call(this, index, &handled);
      if (handled) return;
    }
    QTabBar::tabRemoved(index);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::tabLayoutChange()
  void tabLayoutChange() override {
    if (taken[6]) {
      int handled = 0;
      CuteQTabBarCall6 call = reinterpret_cast<CuteQTabBarCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QTabBar::tabLayoutChange();
  }
#endif  // QT_CONFIG(tabbar)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
  //  bool QTabBar::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTabBarCall7 call = reinterpret_cast<CuteQTabBarCall7>(taken[7]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QTabBar::event(a0);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(tabbar)
  //  void QTabBar::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTabBarCall8 call = reinterpret_cast<CuteQTabBarCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::resizeEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTabBarCall9 call = reinterpret_cast<CuteQTabBarCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::showEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTabBarCall10 call = reinterpret_cast<CuteQTabBarCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::hideEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTabBarCall11 call = reinterpret_cast<CuteQTabBarCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::paintEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTabBarCall12 call = reinterpret_cast<CuteQTabBarCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::mousePressEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTabBarCall13 call = reinterpret_cast<CuteQTabBarCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::mouseMoveEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTabBarCall14 call = reinterpret_cast<CuteQTabBarCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::mouseReleaseEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTabBarCall15 call = reinterpret_cast<CuteQTabBarCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::mouseDoubleClickEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(tabbar)
  //  void QTabBar::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTabBarCall16 call = reinterpret_cast<CuteQTabBarCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTabBar::wheelEvent(event);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(tabbar)
  //  void QTabBar::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTabBarCall17 call = reinterpret_cast<CuteQTabBarCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
  //  void QTabBar::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTabBarCall18 call = reinterpret_cast<CuteQTabBarCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTabBar::changeEvent(a0);
  }
#endif  // QT_CONFIG(tabbar)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tabbar)
  //  void QTabBar::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTabBarCall19 call = reinterpret_cast<CuteQTabBarCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTabBar::timerEvent(event);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(tabbar)
  //  void QTabBar::initStyleOption(QStyleOptionTab *option, int tabIndex)
  //      const
  void initStyleOption(
      QStyleOptionTab *option,
      int tabIndex) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQTabBarCall20 call = reinterpret_cast<CuteQTabBarCall20>(taken[20]);
      call(this, option, tabIndex, &handled);
      if (handled) return;
    }
    QTabBar::initStyleOption(option, tabIndex);
  }
#endif  // QT_CONFIG(tabbar)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTabBarCall21 call = reinterpret_cast<CuteQTabBarCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[22]) {
      int handled = 0;
      CuteQTabBarCall22 call = reinterpret_cast<CuteQTabBarCall22>(taken[22]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQTabBarCall23 call = reinterpret_cast<CuteQTabBarCall23>(taken[23]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQTabBarCall24 call = reinterpret_cast<CuteQTabBarCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQTabBarCall25 call = reinterpret_cast<CuteQTabBarCall25>(taken[25]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTabBarCall26 call = reinterpret_cast<CuteQTabBarCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTabBarCall27 call = reinterpret_cast<CuteQTabBarCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQTabBarCall28 call = reinterpret_cast<CuteQTabBarCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQTabBarCall29 call = reinterpret_cast<CuteQTabBarCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQTabBarCall30 call = reinterpret_cast<CuteQTabBarCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTabBarCall31 call = reinterpret_cast<CuteQTabBarCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQTabBarCall32 call = reinterpret_cast<CuteQTabBarCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTabBarCall33 call = reinterpret_cast<CuteQTabBarCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQTabBarCall34 call = reinterpret_cast<CuteQTabBarCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQTabBarCall35 call = reinterpret_cast<CuteQTabBarCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQTabBarCall36 call = reinterpret_cast<CuteQTabBarCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQTabBarCall37 call = reinterpret_cast<CuteQTabBarCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQTabBarCall38 call = reinterpret_cast<CuteQTabBarCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQTabBarCall39 call = reinterpret_cast<CuteQTabBarCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQTabBarCall40 call = reinterpret_cast<CuteQTabBarCall40>(taken[40]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQTabBarCall41 call = reinterpret_cast<CuteQTabBarCall41>(taken[41]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQTabBarCall42 call = reinterpret_cast<CuteQTabBarCall42>(taken[42]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQTabBarCall43 call = reinterpret_cast<CuteQTabBarCall43>(taken[43]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQTabBarCall44 call = reinterpret_cast<CuteQTabBarCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQTabBarCall45 call = reinterpret_cast<CuteQTabBarCall45>(taken[45]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTabBarCall46 call = reinterpret_cast<CuteQTabBarCall46>(taken[46]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQTabBarCall47 call = reinterpret_cast<CuteQTabBarCall47>(taken[47]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQTabBarCall48 call = reinterpret_cast<CuteQTabBarCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQTabBarCall49 call = reinterpret_cast<CuteQTabBarCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[50]) {
      int handled = 0;
      CuteQTabBarCall50 call = reinterpret_cast<CuteQTabBarCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQTabBarCall51 call = reinterpret_cast<CuteQTabBarCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTabBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QTabBar10metaObjectEv(const QTabBar *self) {
  return self->metaObject();
}

//  QString QTabBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QTabBar2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QTabBar::tr(s, c, n));
}

//  QTabBar::QTabBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTabBar *ritual_ZN7QTabBarC1EP7QWidget(QWidget *parent) {
  return new CuteQTabBar(parent);
}

//  QTabBar::~QTabBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBarD1Ev(QTabBar *self) {
  delete self;
}

//  Shape QTabBar::shape() const
extern "C" Q_DECL_EXPORT
QTabBar::Shape ritual_ZNK7QTabBar5shapeEv(const QTabBar *self) {
  return self->shape();
}

//  void QTabBar::setShape(Shape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar8setShapeENS_5ShapeE(
    QTabBar *self,
    QTabBar::Shape shape) {
  self->setShape(shape);
}

//  int QTabBar::addTab(const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QTabBar6addTabERK7QString(QTabBar *self, const QString *text) {
  return self->addTab(*text);
}

//  int QTabBar::addTab(const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QTabBar6addTabERK5QIconRK7QString(
    QTabBar *self,
    const QIcon *icon,
    const QString *text) {
  return self->addTab(*icon, *text);
}

//  int QTabBar::insertTab(int index, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QTabBar9insertTabEiRK7QString(
    QTabBar *self,
    int index,
    const QString *text) {
  return self->insertTab(index, *text);
}

//  int QTabBar::insertTab(int index, const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QTabBar9insertTabEiRK5QIconRK7QString(
    QTabBar *self,
    int index,
    const QIcon *icon,
    const QString *text) {
  return self->insertTab(index, *icon, *text);
}

//  void QTabBar::removeTab(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar9removeTabEi(QTabBar *self, int index) {
  self->removeTab(index);
}

//  void QTabBar::moveTab(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar7moveTabEii(QTabBar *self, int from, int to) {
  self->moveTab(from, to);
}

//  bool QTabBar::isTabEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar12isTabEnabledEi(const QTabBar *self, int index) {
  return self->isTabEnabled(index);
}

//  void QTabBar::setTabEnabled(int index, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar13setTabEnabledEib(
    QTabBar *self,
    int index,
    bool enabled) {
  self->setTabEnabled(index, enabled);
}

//  bool QTabBar::isTabVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar12isTabVisibleEi(const QTabBar *self, int index) {
  return self->isTabVisible(index);
}

//  void QTabBar::setTabVisible(int index, bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar13setTabVisibleEib(
    QTabBar *self,
    int index,
    bool visible) {
  self->setTabVisible(index, visible);
}

//  QString QTabBar::tabText(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QTabBar7tabTextEi(const QTabBar *self, int index) {
  return new QString(self->tabText(index));
}

//  void QTabBar::setTabText(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10setTabTextEiRK7QString(
    QTabBar *self,
    int index,
    const QString *text) {
  self->setTabText(index, *text);
}

//  QColor QTabBar::tabTextColor(int index) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK7QTabBar12tabTextColorEi(const QTabBar *self, int index) {
  return new QColor(self->tabTextColor(index));
}

//  void QTabBar::setTabTextColor(int index, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setTabTextColorEiRK6QColor(
    QTabBar *self,
    int index,
    const QColor *color) {
  self->setTabTextColor(index, *color);
}

//  QIcon QTabBar::tabIcon(int index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK7QTabBar7tabIconEi(const QTabBar *self, int index) {
  return new QIcon(self->tabIcon(index));
}

//  void QTabBar::setTabIcon(int index, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10setTabIconEiRK5QIcon(
    QTabBar *self,
    int index,
    const QIcon *icon) {
  self->setTabIcon(index, *icon);
}

//  Qt::TextElideMode QTabBar::elideMode() const
extern "C" Q_DECL_EXPORT
Qt::TextElideMode ritual_ZNK7QTabBar9elideModeEv(const QTabBar *self) {
  return self->elideMode();
}

//  void QTabBar::setElideMode(Qt::TextElideMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar12setElideModeEN2Qt13TextElideModeE(
    QTabBar *self,
    Qt::TextElideMode mode) {
  self->setElideMode(mode);
}

#if QT_CONFIG(tooltip)
//  void QTabBar::setTabToolTip(int index, const QString &tip)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar13setTabToolTipEiRK7QString(
    QTabBar *self,
    int index,
    const QString *tip) {
  self->setTabToolTip(index, *tip);
}
#endif  // QT_CONFIG(tooltip)

#if QT_CONFIG(tooltip)
//  QString QTabBar::tabToolTip(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QTabBar10tabToolTipEi(const QTabBar *self, int index) {
  return new QString(self->tabToolTip(index));
}
#endif  // QT_CONFIG(tooltip)

#if QT_CONFIG(whatsthis)
//  void QTabBar::setTabWhatsThis(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setTabWhatsThisEiRK7QString(
    QTabBar *self,
    int index,
    const QString *text) {
  self->setTabWhatsThis(index, *text);
}
#endif  // QT_CONFIG(whatsthis)

#if QT_CONFIG(whatsthis)
//  QString QTabBar::tabWhatsThis(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QTabBar12tabWhatsThisEi(const QTabBar *self, int index) {
  return new QString(self->tabWhatsThis(index));
}
#endif  // QT_CONFIG(whatsthis)

//  void QTabBar::setTabData(int index, const QVariant &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10setTabDataEiRK8QVariant(
    QTabBar *self,
    int index,
    const QVariant *data) {
  self->setTabData(index, *data);
}

//  QVariant QTabBar::tabData(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QTabBar7tabDataEi(const QTabBar *self, int index) {
  return new QVariant(self->tabData(index));
}

//  QRect QTabBar::tabRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QTabBar7tabRectEi(const QTabBar *self, int index) {
  return new QRect(self->tabRect(index));
}

//  int QTabBar::tabAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QTabBar5tabAtERK6QPoint(
    const QTabBar *self,
    const QPoint *pos) {
  return self->tabAt(*pos);
}

//  int QTabBar::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QTabBar12currentIndexEv(const QTabBar *self) {
  return self->currentIndex();
}

//  int QTabBar::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QTabBar5countEv(const QTabBar *self) {
  return self->count();
}

//  QSize QTabBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QTabBar8sizeHintEv(const QTabBar *self) {
  return new QSize(self->sizeHint());
}

//  QSize QTabBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QTabBar15minimumSizeHintEv(const QTabBar *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QTabBar::setDrawBase(bool drawTheBase)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11setDrawBaseEb(QTabBar *self, bool drawTheBase) {
  self->setDrawBase(drawTheBase);
}

//  bool QTabBar::drawBase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar8drawBaseEv(const QTabBar *self) {
  return self->drawBase();
}

//  QSize QTabBar::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QTabBar8iconSizeEv(const QTabBar *self) {
  return new QSize(self->iconSize());
}

//  void QTabBar::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11setIconSizeERK5QSize(
    QTabBar *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  bool QTabBar::usesScrollButtons() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar17usesScrollButtonsEv(const QTabBar *self) {
  return self->usesScrollButtons();
}

//  void QTabBar::setUsesScrollButtons(bool useButtons)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar20setUsesScrollButtonsEb(
    QTabBar *self,
    bool useButtons) {
  self->setUsesScrollButtons(useButtons);
}

//  bool QTabBar::tabsClosable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar12tabsClosableEv(const QTabBar *self) {
  return self->tabsClosable();
}

//  void QTabBar::setTabsClosable(bool closable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setTabsClosableEb(QTabBar *self, bool closable) {
  self->setTabsClosable(closable);
}

//  void QTabBar::setTabButton(int index, ButtonPosition position, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar12setTabButtonEiNS_14ButtonPositionEP7QWidget(
    QTabBar *self,
    int index,
    QTabBar::ButtonPosition position,
    QWidget *widget) {
  self->setTabButton(index, position, widget);
}

//  QWidget *QTabBar::tabButton(int index, ButtonPosition position) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QTabBar9tabButtonEiNS_14ButtonPositionE(
    const QTabBar *self,
    int index,
    QTabBar::ButtonPosition position) {
  return self->tabButton(index, position);
}

//  SelectionBehavior QTabBar::selectionBehaviorOnRemove() const
extern "C" Q_DECL_EXPORT
QTabBar::SelectionBehavior ritual_ZNK7QTabBar25selectionBehaviorOnRemoveEv(
    const QTabBar *self) {
  return self->selectionBehaviorOnRemove();
}

//  void QTabBar::setSelectionBehaviorOnRemove(SelectionBehavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar28setSelectionBehaviorOnRemoveENS_17SelectionBehaviorE(
    QTabBar *self,
    QTabBar::SelectionBehavior behavior) {
  self->setSelectionBehaviorOnRemove(behavior);
}

//  bool QTabBar::expanding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar9expandingEv(const QTabBar *self) {
  return self->expanding();
}

//  void QTabBar::setExpanding(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar12setExpandingEb(QTabBar *self, bool enabled) {
  self->setExpanding(enabled);
}

//  bool QTabBar::isMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar9isMovableEv(const QTabBar *self) {
  return self->isMovable();
}

//  void QTabBar::setMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10setMovableEb(QTabBar *self, bool movable) {
  self->setMovable(movable);
}

//  bool QTabBar::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar12documentModeEv(const QTabBar *self) {
  return self->documentMode();
}

//  void QTabBar::setDocumentMode(bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setDocumentModeEb(QTabBar *self, bool set) {
  self->setDocumentMode(set);
}

//  bool QTabBar::autoHide() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar8autoHideEv(const QTabBar *self) {
  return self->autoHide();
}

//  void QTabBar::setAutoHide(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11setAutoHideEb(QTabBar *self, bool hide) {
  self->setAutoHide(hide);
}

//  bool QTabBar::changeCurrentOnDrag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar19changeCurrentOnDragEv(const QTabBar *self) {
  return self->changeCurrentOnDrag();
}

//  void QTabBar::setChangeCurrentOnDrag(bool change)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar22setChangeCurrentOnDragEb(
    QTabBar *self,
    bool change) {
  self->setChangeCurrentOnDrag(change);
}

#if QT_CONFIG(accessibility)
//  QString QTabBar::accessibleTabName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QTabBar17accessibleTabNameEi(
    const QTabBar *self,
    int index) {
  return new QString(self->accessibleTabName(index));
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QTabBar::setAccessibleTabName(int index, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar20setAccessibleTabNameEiRK7QString(
    QTabBar *self,
    int index,
    const QString *name) {
  self->setAccessibleTabName(index, *name);
}
#endif  // QT_CONFIG(accessibility)

//  void QTabBar::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setCurrentIndexEi(QTabBar *self, int index) {
  self->setCurrentIndex(index);
}

//  QSize QTabBar::tabSizeHint(int index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QTabBar11tabSizeHintEi(const QTabBar *self, int index) {
  return new QSize(self->tabSizeHint(index));
}

//  QSize QTabBar::minimumTabSizeHint(int index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QTabBar18minimumTabSizeHintEi(
    const QTabBar *self,
    int index) {
  return new QSize(self->minimumTabSizeHint(index));
}

//  void QTabBar::tabInserted(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11tabInsertedEi(QTabBar *self, int index) {
  self->tabInserted(index);
}

//  void QTabBar::tabRemoved(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10tabRemovedEi(QTabBar *self, int index) {
  self->tabRemoved(index);
}

//  void QTabBar::tabLayoutChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15tabLayoutChangeEv(QTabBar *self) {
  self->tabLayoutChange();
}

//  bool QTabBar::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QTabBar5eventEP6QEvent(QTabBar *self, QEvent *a0) {
  return self->event(a0);
}

//  void QTabBar::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11resizeEventEP12QResizeEvent(
    QTabBar *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QTabBar::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar9showEventEP10QShowEvent(
    QTabBar *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void QTabBar::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar9hideEventEP10QHideEvent(
    QTabBar *self,
    QHideEvent *a0) {
  self->hideEvent(a0);
}

//  void QTabBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10paintEventEP11QPaintEvent(
    QTabBar *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QTabBar::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15mousePressEventEP11QMouseEvent(
    QTabBar *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QTabBar::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar14mouseMoveEventEP11QMouseEvent(
    QTabBar *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  void QTabBar::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar17mouseReleaseEventEP11QMouseEvent(
    QTabBar *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QTabBar::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar21mouseDoubleClickEventEP11QMouseEvent(
    QTabBar *self,
    QMouseEvent *a0) {
  self->mouseDoubleClickEvent(a0);
}

#if QT_CONFIG(wheelevent)
//  void QTabBar::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10wheelEventEP11QWheelEvent(
    QTabBar *self,
    QWheelEvent *event) {
  self->wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QTabBar::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar13keyPressEventEP9QKeyEvent(
    QTabBar *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QTabBar::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11changeEventEP6QEvent(QTabBar *self, QEvent *a0) {
  self->changeEvent(a0);
}

//  void QTabBar::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10timerEventEP11QTimerEvent(
    QTabBar *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QTabBar::initStyleOption(QStyleOptionTab *option, int tabIndex)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QTabBar15initStyleOptionEP15QStyleOptionTabi(
    const QTabBar *self,
    QStyleOptionTab *option,
    int tabIndex) {
  self->initStyleOption(option, tabIndex);
}

//  QTabBarPrivate *QTabBar::d_func()
extern "C" Q_DECL_EXPORT
QTabBarPrivate *ritual_ZN7QTabBar6d_funcEv(QTabBar *self) {
  return self->d_func();
}

//  const QTabBarPrivate *QTabBar::d_func() const
extern "C" Q_DECL_EXPORT
const QTabBarPrivate *ritual_ZNK7QTabBar6d_funcEv(const QTabBar *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTabBar, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTabBar(QTabBar *self, const char *key, void *call) {
  return static_cast<CuteQTabBar *>(self)->take(key, call);
}

//  QSize QTabBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QTabBar8sizeHintEv(const QTabBar *self) {
  return new QSize(self->QTabBar::sizeHint());
}

//  QSize QTabBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QTabBar15minimumSizeHintEv(const QTabBar *self) {
  return new QSize(self->QTabBar::minimumSizeHint());
}

//  QSize QTabBar::tabSizeHint(int index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QTabBar11tabSizeHintEi(
    const QTabBar *self,
    int index) {
  return new QSize(
      static_cast<const OwnQTabBar *>(self)->OwnQTabBar::tabSizeHint(
          index));
}

//  QSize QTabBar::minimumTabSizeHint(int index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QTabBar18minimumTabSizeHintEi(
    const QTabBar *self,
    int index) {
  return new QSize(
      static_cast<const OwnQTabBar *>(self)->OwnQTabBar::minimumTabSizeHint(
          index));
}

//  void QTabBar::tabInserted(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar11tabInsertedEi(QTabBar *self, int index) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::tabInserted(index);
}

//  void QTabBar::tabRemoved(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar10tabRemovedEi(QTabBar *self, int index) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::tabRemoved(index);
}

//  void QTabBar::tabLayoutChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar15tabLayoutChangeEv(QTabBar *self) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::tabLayoutChange();
}

//  bool QTabBar::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QTabBar5eventEP6QEvent(QTabBar *self, QEvent *a0) {
  return static_cast<OwnQTabBar *>(self)->OwnQTabBar::event(a0);
}

//  void QTabBar::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar11resizeEventEP12QResizeEvent(
    QTabBar *self,
    QResizeEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::resizeEvent(a0);
}

//  void QTabBar::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar9showEventEP10QShowEvent(
    QTabBar *self,
    QShowEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::showEvent(a0);
}

//  void QTabBar::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar9hideEventEP10QHideEvent(
    QTabBar *self,
    QHideEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::hideEvent(a0);
}

//  void QTabBar::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar10paintEventEP11QPaintEvent(
    QTabBar *self,
    QPaintEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::paintEvent(a0);
}

//  void QTabBar::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar15mousePressEventEP11QMouseEvent(
    QTabBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::mousePressEvent(a0);
}

//  void QTabBar::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar14mouseMoveEventEP11QMouseEvent(
    QTabBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::mouseMoveEvent(a0);
}

//  void QTabBar::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar17mouseReleaseEventEP11QMouseEvent(
    QTabBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::mouseReleaseEvent(a0);
}

//  void QTabBar::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar21mouseDoubleClickEventEP11QMouseEvent(
    QTabBar *self,
    QMouseEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::mouseDoubleClickEvent(a0);
}

#if QT_CONFIG(wheelevent)
//  void QTabBar::wheelEvent(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar10wheelEventEP11QWheelEvent(
    QTabBar *self,
    QWheelEvent *event) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::wheelEvent(event);
}
#endif  // QT_CONFIG(wheelevent)

//  void QTabBar::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar13keyPressEventEP9QKeyEvent(
    QTabBar *self,
    QKeyEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::keyPressEvent(a0);
}

//  void QTabBar::changeEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar11changeEventEP6QEvent(QTabBar *self, QEvent *a0) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::changeEvent(a0);
}

//  void QTabBar::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QTabBar10timerEventEP11QTimerEvent(
    QTabBar *self,
    QTimerEvent *event) {
  static_cast<OwnQTabBar *>(self)->OwnQTabBar::timerEvent(event);
}

//  void QTabBar::initStyleOption(QStyleOptionTab *option, int tabIndex)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK7QTabBar15initStyleOptionEP15QStyleOptionTabi(
    const QTabBar *self,
    QStyleOptionTab *option,
    int tabIndex) {
  static_cast<const OwnQTabBar *>(self)->OwnQTabBar::initStyleOption(
      option,
      tabIndex);
}

#endif  // QT_CONFIG(tabbar)
