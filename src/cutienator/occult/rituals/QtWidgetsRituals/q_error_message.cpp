//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qerrormessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(errormessage)
#include <QtWidgets/qerrormessage.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QErrorMessage may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQErrorMessage : QErrorMessage {
  using QErrorMessage::done;
  using QErrorMessage::changeEvent;
};

//  A QErrorMessage that Python can take functions over in. Every QErrorMessage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
#if QT_CONFIG(errormessage)
typedef void (*CuteQErrorMessageCall0)(const void *, int, int *);
#endif  // QT_CONFIG(errormessage)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(errormessage)
typedef void (*CuteQErrorMessageCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(errormessage)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall2)(const void *, bool, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQErrorMessageCall3)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQErrorMessageCall4)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall5)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQErrorMessageCall6)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall7)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall8)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall9)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall10)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall11)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall12)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
typedef void (*CuteQErrorMessageCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
typedef bool (*CuteQErrorMessageCall14)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQErrorMessageCall15)(const void *, int *);
typedef int (*CuteQErrorMessageCall16)(const void *, int, int *);
typedef bool (*CuteQErrorMessageCall17)(const void *, int *);
typedef void * (*CuteQErrorMessageCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQErrorMessageCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQErrorMessageCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQErrorMessageCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQErrorMessageCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQErrorMessageCall23)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQErrorMessageCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQErrorMessageCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQErrorMessageCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQErrorMessageCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQErrorMessageCall28)(const void *, QEnterEvent *, int *);
typedef void (*CuteQErrorMessageCall29)(const void *, QEvent *, int *);
typedef void (*CuteQErrorMessageCall30)(const void *, QPaintEvent *, int *);
typedef void (*CuteQErrorMessageCall31)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQErrorMessageCall32)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQErrorMessageCall33)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQErrorMessageCall34)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQErrorMessageCall35)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQErrorMessageCall36)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQErrorMessageCall37)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQErrorMessageCall38)(const void *, QHideEvent *, int *);
typedef int (*CuteQErrorMessageCall39)(const void *, int, int *);
typedef void (*CuteQErrorMessageCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQErrorMessageCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQErrorMessageCall42)(const void *, int *);
typedef void (*CuteQErrorMessageCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQErrorMessageCall44)(const void *, int, int *);
typedef bool (*CuteQErrorMessageCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQErrorMessageCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQErrorMessageCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQErrorMessageCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQErrorMessageCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQErrorMessageCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQErrorMessage : public QErrorMessage {
public:
  using QErrorMessage::QErrorMessage;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dialog)
#if QT_CONFIG(errormessage)
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(errormessage)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(errormessage)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(errormessage)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[31] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
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

#if QT_CONFIG(dialog)
#if QT_CONFIG(errormessage)
  //  void QErrorMessage::done(int a0)
  void done(int a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQErrorMessageCall0 call = reinterpret_cast<CuteQErrorMessageCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QErrorMessage::done(a0);
  }
#endif  // QT_CONFIG(errormessage)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(errormessage)
  //  void QErrorMessage::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQErrorMessageCall1 call = reinterpret_cast<CuteQErrorMessageCall1>(taken[1]);
      call(this, e, &handled);
      if (handled) return;
    }
    QErrorMessage::changeEvent(e);
  }
#endif  // QT_CONFIG(errormessage)

#if QT_CONFIG(dialog)
  //  void QDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQErrorMessageCall2 call = reinterpret_cast<CuteQErrorMessageCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDialog::setVisible(visible);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQErrorMessageCall3 call = reinterpret_cast<CuteQErrorMessageCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQErrorMessageCall4 call = reinterpret_cast<CuteQErrorMessageCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::open()
  void open() override {
    if (taken[5]) {
      int handled = 0;
      CuteQErrorMessageCall5 call = reinterpret_cast<CuteQErrorMessageCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialog::exec()
  int exec() override {
    if (taken[6]) {
      int handled = 0;
      CuteQErrorMessageCall6 call = reinterpret_cast<CuteQErrorMessageCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::accept()
  void accept() override {
    if (taken[7]) {
      int handled = 0;
      CuteQErrorMessageCall7 call = reinterpret_cast<CuteQErrorMessageCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::reject()
  void reject() override {
    if (taken[8]) {
      int handled = 0;
      CuteQErrorMessageCall8 call = reinterpret_cast<CuteQErrorMessageCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQErrorMessageCall9 call = reinterpret_cast<CuteQErrorMessageCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQErrorMessageCall10 call = reinterpret_cast<CuteQErrorMessageCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQErrorMessageCall11 call = reinterpret_cast<CuteQErrorMessageCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQErrorMessageCall12 call = reinterpret_cast<CuteQErrorMessageCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::resizeEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQErrorMessageCall13 call = reinterpret_cast<CuteQErrorMessageCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
  //  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQErrorMessageCall14 call = reinterpret_cast<CuteQErrorMessageCall14>(taken[14]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQErrorMessageCall15 call = reinterpret_cast<CuteQErrorMessageCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQErrorMessageCall16 call = reinterpret_cast<CuteQErrorMessageCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQErrorMessageCall17 call = reinterpret_cast<CuteQErrorMessageCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQErrorMessageCall18 call = reinterpret_cast<CuteQErrorMessageCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQErrorMessageCall19 call = reinterpret_cast<CuteQErrorMessageCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQErrorMessageCall20 call = reinterpret_cast<CuteQErrorMessageCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQErrorMessageCall21 call = reinterpret_cast<CuteQErrorMessageCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQErrorMessageCall22 call = reinterpret_cast<CuteQErrorMessageCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQErrorMessageCall23 call = reinterpret_cast<CuteQErrorMessageCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQErrorMessageCall24 call = reinterpret_cast<CuteQErrorMessageCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQErrorMessageCall25 call = reinterpret_cast<CuteQErrorMessageCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQErrorMessageCall26 call = reinterpret_cast<CuteQErrorMessageCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQErrorMessageCall27 call = reinterpret_cast<CuteQErrorMessageCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQErrorMessageCall28 call = reinterpret_cast<CuteQErrorMessageCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQErrorMessageCall29 call = reinterpret_cast<CuteQErrorMessageCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQErrorMessageCall30 call = reinterpret_cast<CuteQErrorMessageCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQErrorMessageCall31 call = reinterpret_cast<CuteQErrorMessageCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQErrorMessageCall32 call = reinterpret_cast<CuteQErrorMessageCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQErrorMessageCall33 call = reinterpret_cast<CuteQErrorMessageCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQErrorMessageCall34 call = reinterpret_cast<CuteQErrorMessageCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQErrorMessageCall35 call = reinterpret_cast<CuteQErrorMessageCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQErrorMessageCall36 call = reinterpret_cast<CuteQErrorMessageCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQErrorMessageCall37 call = reinterpret_cast<CuteQErrorMessageCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQErrorMessageCall38 call = reinterpret_cast<CuteQErrorMessageCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQErrorMessageCall39 call = reinterpret_cast<CuteQErrorMessageCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQErrorMessageCall40 call = reinterpret_cast<CuteQErrorMessageCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQErrorMessageCall41 call = reinterpret_cast<CuteQErrorMessageCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQErrorMessageCall42 call = reinterpret_cast<CuteQErrorMessageCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQErrorMessageCall43 call = reinterpret_cast<CuteQErrorMessageCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQErrorMessageCall44 call = reinterpret_cast<CuteQErrorMessageCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQErrorMessageCall45 call = reinterpret_cast<CuteQErrorMessageCall45>(taken[45]);
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
      CuteQErrorMessageCall46 call = reinterpret_cast<CuteQErrorMessageCall46>(taken[46]);
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
      CuteQErrorMessageCall47 call = reinterpret_cast<CuteQErrorMessageCall47>(taken[47]);
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
      CuteQErrorMessageCall48 call = reinterpret_cast<CuteQErrorMessageCall48>(taken[48]);
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
      CuteQErrorMessageCall49 call = reinterpret_cast<CuteQErrorMessageCall49>(taken[49]);
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
      CuteQErrorMessageCall50 call = reinterpret_cast<CuteQErrorMessageCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QErrorMessage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QErrorMessage10metaObjectEv(
    const QErrorMessage *self) {
  return self->metaObject();
}

//  QString QErrorMessage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QErrorMessage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QErrorMessage::tr(s, c, n));
}

//  QErrorMessage::QErrorMessage(QWidget *parent)
extern "C" Q_DECL_EXPORT
QErrorMessage *ritual_ZN13QErrorMessageC1EP7QWidget(QWidget *parent) {
  return new CuteQErrorMessage(parent);
}

//  QErrorMessage::~QErrorMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QErrorMessageD1Ev(QErrorMessage *self) {
  delete self;
}

//  QErrorMessage *QErrorMessage::qtHandler()
extern "C" Q_DECL_EXPORT
QErrorMessage *ritual_ZN13QErrorMessage9qtHandlerEv() {
  return QErrorMessage::qtHandler();
}

//  void QErrorMessage::showMessage(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QErrorMessage11showMessageERK7QString(
    QErrorMessage *self,
    const QString *message) {
  self->showMessage(*message);
}

//  void QErrorMessage::showMessage(const QString &message, const QString
//      &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QErrorMessage11showMessageERK7QStringS2_(
    QErrorMessage *self,
    const QString *message,
    const QString *type) {
  self->showMessage(*message, *type);
}

//  void QErrorMessage::done(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QErrorMessage4doneEi(QErrorMessage *self, int a0) {
  self->done(a0);
}

//  void QErrorMessage::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QErrorMessage11changeEventEP6QEvent(
    QErrorMessage *self,
    QEvent *e) {
  self->changeEvent(e);
}

//  a Python function taken by a CuteQErrorMessage, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QErrorMessage(
    QErrorMessage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQErrorMessage *>(self)->take(key, call);
}

//  void QErrorMessage::done(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QErrorMessage4doneEi(QErrorMessage *self, int a0) {
  static_cast<OwnQErrorMessage *>(self)->OwnQErrorMessage::done(a0);
}

//  void QErrorMessage::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QErrorMessage11changeEventEP6QEvent(
    QErrorMessage *self,
    QEvent *e) {
  static_cast<OwnQErrorMessage *>(self)->OwnQErrorMessage::changeEvent(e);
}

#endif  // QT_CONFIG(errormessage)
