//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfontcombobox.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(fontcombobox)
#include <QtWidgets/qfontcombobox.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QFontComboBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFontComboBox : QFontComboBox {
  using QFontComboBox::event;
};

//  A QFontComboBox that Python can take functions over in. Every QFontComboBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(fontcombobox)
typedef const QSize * (*CuteQFontComboBoxCall0)(const void *, int *);
#endif  // QT_CONFIG(fontcombobox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(fontcombobox)
typedef bool (*CuteQFontComboBoxCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(fontcombobox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall2)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef const QSize * (*CuteQFontComboBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall4)(const void *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall5)(const void *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef const QVariant * (*CuteQFontComboBoxCall6)(const void *, int, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall7)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall8)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall9)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall10)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall11)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall12)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall13)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall14)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall15)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall16)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall17)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall18)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall19)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall20)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQFontComboBoxCall21)(const void *, QStyleOptionComboBox *, int *);
#endif  // QT_CONFIG(combobox)
typedef int (*CuteQFontComboBoxCall22)(const void *, int *);
typedef void (*CuteQFontComboBoxCall23)(const void *, bool, int *);
typedef int (*CuteQFontComboBoxCall24)(const void *, int, int *);
typedef bool (*CuteQFontComboBoxCall25)(const void *, int *);
typedef void * (*CuteQFontComboBoxCall26)(const void *, int *);
typedef void (*CuteQFontComboBoxCall27)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFontComboBoxCall28)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFontComboBoxCall29)(const void *, QEnterEvent *, int *);
typedef void (*CuteQFontComboBoxCall30)(const void *, QEvent *, int *);
typedef void (*CuteQFontComboBoxCall31)(const void *, QMoveEvent *, int *);
typedef void (*CuteQFontComboBoxCall32)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQFontComboBoxCall33)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQFontComboBoxCall34)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFontComboBoxCall35)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFontComboBoxCall36)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFontComboBoxCall37)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFontComboBoxCall38)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef int (*CuteQFontComboBoxCall39)(const void *, int, int *);
typedef void (*CuteQFontComboBoxCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQFontComboBoxCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQFontComboBoxCall42)(const void *, int *);
typedef bool (*CuteQFontComboBoxCall43)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFontComboBoxCall44)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontComboBoxCall45)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontComboBoxCall46)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontComboBoxCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontComboBoxCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFontComboBoxCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFontComboBox : public QFontComboBox {
public:
  using QFontComboBox::QFontComboBox;
  void *taken[50] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(fontcombobox)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(fontcombobox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(fontcombobox)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(fontcombobox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN9QComboBox8setModelEP18QAbstractItemModel")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN9QComboBox9showPopupEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN9QComboBox9hidePopupEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK9QComboBox15initStyleOptionEP20QStyleOptionComboBox")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
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
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
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
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[43] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(fontcombobox)
  //  QSize QFontComboBox::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontComboBoxCall0 call = reinterpret_cast<CuteQFontComboBoxCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontComboBox::sizeHint();
  }
#endif  // QT_CONFIG(fontcombobox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(fontcombobox)
  //  bool QFontComboBox::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontComboBoxCall1 call = reinterpret_cast<CuteQFontComboBoxCall1>(taken[1]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QFontComboBox::event(e);
  }
#endif  // QT_CONFIG(fontcombobox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(combobox)
  //  void QComboBox::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontComboBoxCall2 call = reinterpret_cast<CuteQFontComboBoxCall2>(taken[2]);
      call(this, model, &handled);
      if (handled) return;
    }
    QComboBox::setModel(model);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  QSize QComboBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontComboBoxCall3 call = reinterpret_cast<CuteQFontComboBoxCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QComboBox::minimumSizeHint();
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::showPopup()
  void showPopup() override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontComboBoxCall4 call = reinterpret_cast<CuteQFontComboBoxCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QComboBox::showPopup();
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::hidePopup()
  void hidePopup() override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontComboBoxCall5 call = reinterpret_cast<CuteQFontComboBoxCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QComboBox::hidePopup();
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  QVariant QComboBox::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontComboBoxCall6 call = reinterpret_cast<CuteQFontComboBoxCall6>(taken[6]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QComboBox::inputMethodQuery(a0);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontComboBoxCall7 call = reinterpret_cast<CuteQFontComboBoxCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::focusInEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontComboBoxCall8 call = reinterpret_cast<CuteQFontComboBoxCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::focusOutEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontComboBoxCall9 call = reinterpret_cast<CuteQFontComboBoxCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::changeEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontComboBoxCall10 call = reinterpret_cast<CuteQFontComboBoxCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::resizeEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontComboBoxCall11 call = reinterpret_cast<CuteQFontComboBoxCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::paintEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::showEvent(QShowEvent *e)
  void showEvent(QShowEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontComboBoxCall12 call = reinterpret_cast<CuteQFontComboBoxCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::showEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::hideEvent(QHideEvent *e)
  void hideEvent(QHideEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontComboBoxCall13 call = reinterpret_cast<CuteQFontComboBoxCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::hideEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQFontComboBoxCall14 call = reinterpret_cast<CuteQFontComboBoxCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::mousePressEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQFontComboBoxCall15 call = reinterpret_cast<CuteQFontComboBoxCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQFontComboBoxCall16 call = reinterpret_cast<CuteQFontComboBoxCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::keyPressEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFontComboBoxCall17 call = reinterpret_cast<CuteQFontComboBoxCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::keyReleaseEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(combobox)
  //  void QComboBox::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFontComboBoxCall18 call = reinterpret_cast<CuteQFontComboBoxCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::wheelEvent(e);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(combobox)
  //  void QComboBox::contextMenuEvent(QContextMenuEvent *e)
  void contextMenuEvent(QContextMenuEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFontComboBoxCall19 call = reinterpret_cast<CuteQFontComboBoxCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBox::contextMenuEvent(e);
  }
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(combobox)
  //  void QComboBox::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQFontComboBoxCall20 call = reinterpret_cast<CuteQFontComboBoxCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QComboBox::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBox::initStyleOption(QStyleOptionComboBox *option) const
  void initStyleOption(QStyleOptionComboBox *option) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQFontComboBoxCall21 call = reinterpret_cast<CuteQFontComboBoxCall21>(taken[21]);
      call(this, option, &handled);
      if (handled) return;
    }
    QComboBox::initStyleOption(option);
  }
#endif  // QT_CONFIG(combobox)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQFontComboBoxCall22 call = reinterpret_cast<CuteQFontComboBoxCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFontComboBoxCall23 call = reinterpret_cast<CuteQFontComboBoxCall23>(taken[23]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQFontComboBoxCall24 call = reinterpret_cast<CuteQFontComboBoxCall24>(taken[24]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQFontComboBoxCall25 call = reinterpret_cast<CuteQFontComboBoxCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQFontComboBoxCall26 call = reinterpret_cast<CuteQFontComboBoxCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQFontComboBoxCall27 call = reinterpret_cast<CuteQFontComboBoxCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFontComboBoxCall28 call = reinterpret_cast<CuteQFontComboBoxCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFontComboBoxCall29 call = reinterpret_cast<CuteQFontComboBoxCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQFontComboBoxCall30 call = reinterpret_cast<CuteQFontComboBoxCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQFontComboBoxCall31 call = reinterpret_cast<CuteQFontComboBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQFontComboBoxCall32 call = reinterpret_cast<CuteQFontComboBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQFontComboBoxCall33 call = reinterpret_cast<CuteQFontComboBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQFontComboBoxCall34 call = reinterpret_cast<CuteQFontComboBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQFontComboBoxCall35 call = reinterpret_cast<CuteQFontComboBoxCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQFontComboBoxCall36 call = reinterpret_cast<CuteQFontComboBoxCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQFontComboBoxCall37 call = reinterpret_cast<CuteQFontComboBoxCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQFontComboBoxCall38 call = reinterpret_cast<CuteQFontComboBoxCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFontComboBoxCall39 call = reinterpret_cast<CuteQFontComboBoxCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQFontComboBoxCall40 call = reinterpret_cast<CuteQFontComboBoxCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQFontComboBoxCall41 call = reinterpret_cast<CuteQFontComboBoxCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQFontComboBoxCall42 call = reinterpret_cast<CuteQFontComboBoxCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[43]) {
      int handled = 0;
      CuteQFontComboBoxCall43 call = reinterpret_cast<CuteQFontComboBoxCall43>(taken[43]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQFontComboBoxCall44 call = reinterpret_cast<CuteQFontComboBoxCall44>(taken[44]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQFontComboBoxCall45 call = reinterpret_cast<CuteQFontComboBoxCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQFontComboBoxCall46 call = reinterpret_cast<CuteQFontComboBoxCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQFontComboBoxCall47 call = reinterpret_cast<CuteQFontComboBoxCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteQFontComboBoxCall48 call = reinterpret_cast<CuteQFontComboBoxCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[49]) {
      int handled = 0;
      CuteQFontComboBoxCall49 call = reinterpret_cast<CuteQFontComboBoxCall49>(taken[49]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFontComboBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QFontComboBox10metaObjectEv(
    const QFontComboBox *self) {
  return self->metaObject();
}

//  QString QFontComboBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFontComboBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFontComboBox::tr(s, c, n));
}

//  QFontComboBox::QFontComboBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFontComboBox *ritual_ZN13QFontComboBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQFontComboBox(parent);
}

//  QFontComboBox::~QFontComboBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBoxD1Ev(QFontComboBox *self) {
  delete self;
}

//  void QFontComboBox::setWritingSystem(QFontDatabase::WritingSystem a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox16setWritingSystemEN13QFontDatabase13WritingSystemE(
    QFontComboBox *self,
    QFontDatabase::WritingSystem a0) {
  self->setWritingSystem(a0);
}

//  QFontDatabase::WritingSystem QFontComboBox::writingSystem() const
extern "C" Q_DECL_EXPORT
QFontDatabase::WritingSystem ritual_ZNK13QFontComboBox13writingSystemEv(
    const QFontComboBox *self) {
  return self->writingSystem();
}

//  void QFontComboBox::setFontFilters(FontFilters filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox14setFontFiltersE6QFlagsINS_10FontFilterEE(
    QFontComboBox *self,
    int filters) {
  self->setFontFilters(QFlags<QFontComboBox::FontFilter>::fromInt(filters));
}

//  FontFilters QFontComboBox::fontFilters() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFontComboBox11fontFiltersEv(const QFontComboBox *self) {
  return static_cast<int>(self->fontFilters().toInt());
}

//  QFont QFontComboBox::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QFontComboBox11currentFontEv(const QFontComboBox *self) {
  return new QFont(self->currentFont());
}

//  QSize QFontComboBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QFontComboBox8sizeHintEv(const QFontComboBox *self) {
  return new QSize(self->sizeHint());
}

//  void QFontComboBox::setSampleTextForSystem(QFontDatabase::WritingSystem
//      writingSystem, const QString &sampleText)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox22setSampleTextForSystemEN13QFontDatabase13WritingSystemERK7QString(
    QFontComboBox *self,
    QFontDatabase::WritingSystem writingSystem,
    const QString *sampleText) {
  self->setSampleTextForSystem(writingSystem, *sampleText);
}

//  QString QFontComboBox::sampleTextForSystem(QFontDatabase::WritingSystem
//      writingSystem) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFontComboBox19sampleTextForSystemEN13QFontDatabase13WritingSystemE(
    const QFontComboBox *self,
    QFontDatabase::WritingSystem writingSystem) {
  return new QString(self->sampleTextForSystem(writingSystem));
}

//  void QFontComboBox::setSampleTextForFont(const QString &fontFamily, const
//      QString &sampleText)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox20setSampleTextForFontERK7QStringS2_(
    QFontComboBox *self,
    const QString *fontFamily,
    const QString *sampleText) {
  self->setSampleTextForFont(*fontFamily, *sampleText);
}

//  QString QFontComboBox::sampleTextForFont(const QString &fontFamily) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFontComboBox17sampleTextForFontERK7QString(
    const QFontComboBox *self,
    const QString *fontFamily) {
  return new QString(self->sampleTextForFont(*fontFamily));
}

//  void QFontComboBox::setDisplayFont(const QString &fontFamily, const QFont
//      &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox14setDisplayFontERK7QStringRK5QFont(
    QFontComboBox *self,
    const QString *fontFamily,
    const QFont *font) {
  self->setDisplayFont(*fontFamily, *font);
}

//  void QFontComboBox::setCurrentFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontComboBox14setCurrentFontERK5QFont(
    QFontComboBox *self,
    const QFont *f) {
  self->setCurrentFont(*f);
}

//  bool QFontComboBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFontComboBox5eventEP6QEvent(
    QFontComboBox *self,
    QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQFontComboBox, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontComboBox(
    QFontComboBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontComboBox *>(self)->take(key, call);
}

//  QSize QFontComboBox::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK13QFontComboBox8sizeHintEv(const QFontComboBox *self) {
  return new QSize(self->QFontComboBox::sizeHint());
}

//  bool QFontComboBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFontComboBox5eventEP6QEvent(
    QFontComboBox *self,
    QEvent *e) {
  return static_cast<OwnQFontComboBox *>(self)->OwnQFontComboBox::event(e);
}

#endif  // QT_CONFIG(fontcombobox)
