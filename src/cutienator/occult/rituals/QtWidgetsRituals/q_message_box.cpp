//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmessagebox.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/qabstractbutton.h>
#endif
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QMessageBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMessageBox : QMessageBox {
  using QMessageBox::event;
  using QMessageBox::resizeEvent;
  using QMessageBox::showEvent;
  using QMessageBox::closeEvent;
  using QMessageBox::keyPressEvent;
  using QMessageBox::changeEvent;
};

//  A QMessageBox that Python can take functions over in. Every QMessageBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(messagebox)
typedef bool (*CuteQMessageBoxCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(messagebox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(messagebox)
typedef void (*CuteQMessageBoxCall1)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
typedef void (*CuteQMessageBoxCall2)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
typedef void (*CuteQMessageBoxCall3)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
typedef void (*CuteQMessageBoxCall4)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
typedef void (*CuteQMessageBoxCall5)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(dialog)
typedef void (*CuteQMessageBoxCall6)(const void *, bool, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQMessageBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQMessageBoxCall8)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQMessageBoxCall9)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQMessageBoxCall10)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQMessageBoxCall11)(const void *, int, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQMessageBoxCall12)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQMessageBoxCall13)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
typedef void (*CuteQMessageBoxCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
typedef bool (*CuteQMessageBoxCall15)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQMessageBoxCall16)(const void *, int *);
typedef int (*CuteQMessageBoxCall17)(const void *, int, int *);
typedef bool (*CuteQMessageBoxCall18)(const void *, int *);
typedef void * (*CuteQMessageBoxCall19)(const void *, int *);
typedef void (*CuteQMessageBoxCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMessageBoxCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMessageBoxCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQMessageBoxCall23)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQMessageBoxCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQMessageBoxCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQMessageBoxCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMessageBoxCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQMessageBoxCall28)(const void *, QEnterEvent *, int *);
typedef void (*CuteQMessageBoxCall29)(const void *, QEvent *, int *);
typedef void (*CuteQMessageBoxCall30)(const void *, QPaintEvent *, int *);
typedef void (*CuteQMessageBoxCall31)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQMessageBoxCall32)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQMessageBoxCall33)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQMessageBoxCall34)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQMessageBoxCall35)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQMessageBoxCall36)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQMessageBoxCall37)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQMessageBoxCall38)(const void *, QHideEvent *, int *);
typedef int (*CuteQMessageBoxCall39)(const void *, int, int *);
typedef void (*CuteQMessageBoxCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQMessageBoxCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQMessageBoxCall42)(const void *, int *);
typedef void (*CuteQMessageBoxCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQMessageBoxCall44)(const void *, int, int *);
typedef bool (*CuteQMessageBoxCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMessageBoxCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMessageBoxCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMessageBoxCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMessageBoxCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMessageBoxCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMessageBox : public QMessageBox {
public:
  using QMessageBox::QMessageBox;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(messagebox)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(messagebox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(messagebox)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(messagebox)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(messagebox)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[19] = call;
      return true;
    }
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

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(messagebox)
  //  bool QMessageBox::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMessageBoxCall0 call = reinterpret_cast<CuteQMessageBoxCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QMessageBox::event(e);
  }
#endif  // QT_CONFIG(messagebox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(messagebox)
  //  void QMessageBox::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMessageBoxCall1 call = reinterpret_cast<CuteQMessageBoxCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QMessageBox::resizeEvent(event);
  }
#endif  // QT_CONFIG(messagebox)

#if QT_CONFIG(messagebox)
  //  void QMessageBox::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMessageBoxCall2 call = reinterpret_cast<CuteQMessageBoxCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QMessageBox::showEvent(event);
  }
#endif  // QT_CONFIG(messagebox)

#if QT_CONFIG(messagebox)
  //  void QMessageBox::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMessageBoxCall3 call = reinterpret_cast<CuteQMessageBoxCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QMessageBox::closeEvent(event);
  }
#endif  // QT_CONFIG(messagebox)

#if QT_CONFIG(messagebox)
  //  void QMessageBox::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMessageBoxCall4 call = reinterpret_cast<CuteQMessageBoxCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QMessageBox::keyPressEvent(event);
  }
#endif  // QT_CONFIG(messagebox)

#if QT_CONFIG(messagebox)
  //  void QMessageBox::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMessageBoxCall5 call = reinterpret_cast<CuteQMessageBoxCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QMessageBox::changeEvent(event);
  }
#endif  // QT_CONFIG(messagebox)

#if QT_CONFIG(dialog)
  //  void QDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMessageBoxCall6 call = reinterpret_cast<CuteQMessageBoxCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDialog::setVisible(visible);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQMessageBoxCall7 call = reinterpret_cast<CuteQMessageBoxCall7>(taken[7]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQMessageBoxCall8 call = reinterpret_cast<CuteQMessageBoxCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::open()
  void open() override {
    if (taken[9]) {
      int handled = 0;
      CuteQMessageBoxCall9 call = reinterpret_cast<CuteQMessageBoxCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialog::exec()
  int exec() override {
    if (taken[10]) {
      int handled = 0;
      CuteQMessageBoxCall10 call = reinterpret_cast<CuteQMessageBoxCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::done(int a0)
  void done(int a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQMessageBoxCall11 call = reinterpret_cast<CuteQMessageBoxCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::done(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::accept()
  void accept() override {
    if (taken[12]) {
      int handled = 0;
      CuteQMessageBoxCall12 call = reinterpret_cast<CuteQMessageBoxCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::reject()
  void reject() override {
    if (taken[13]) {
      int handled = 0;
      CuteQMessageBoxCall13 call = reinterpret_cast<CuteQMessageBoxCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }
#endif  // QT_CONFIG(dialog)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
  //  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQMessageBoxCall14 call = reinterpret_cast<CuteQMessageBoxCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQMessageBoxCall15 call = reinterpret_cast<CuteQMessageBoxCall15>(taken[15]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQMessageBoxCall16 call = reinterpret_cast<CuteQMessageBoxCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQMessageBoxCall17 call = reinterpret_cast<CuteQMessageBoxCall17>(taken[17]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQMessageBoxCall18 call = reinterpret_cast<CuteQMessageBoxCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQMessageBoxCall19 call = reinterpret_cast<CuteQMessageBoxCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQMessageBoxCall20 call = reinterpret_cast<CuteQMessageBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQMessageBoxCall21 call = reinterpret_cast<CuteQMessageBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQMessageBoxCall22 call = reinterpret_cast<CuteQMessageBoxCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQMessageBoxCall23 call = reinterpret_cast<CuteQMessageBoxCall23>(taken[23]);
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
      CuteQMessageBoxCall24 call = reinterpret_cast<CuteQMessageBoxCall24>(taken[24]);
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
      CuteQMessageBoxCall25 call = reinterpret_cast<CuteQMessageBoxCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQMessageBoxCall26 call = reinterpret_cast<CuteQMessageBoxCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQMessageBoxCall27 call = reinterpret_cast<CuteQMessageBoxCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQMessageBoxCall28 call = reinterpret_cast<CuteQMessageBoxCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQMessageBoxCall29 call = reinterpret_cast<CuteQMessageBoxCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQMessageBoxCall30 call = reinterpret_cast<CuteQMessageBoxCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQMessageBoxCall31 call = reinterpret_cast<CuteQMessageBoxCall31>(taken[31]);
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
      CuteQMessageBoxCall32 call = reinterpret_cast<CuteQMessageBoxCall32>(taken[32]);
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
      CuteQMessageBoxCall33 call = reinterpret_cast<CuteQMessageBoxCall33>(taken[33]);
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
      CuteQMessageBoxCall34 call = reinterpret_cast<CuteQMessageBoxCall34>(taken[34]);
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
      CuteQMessageBoxCall35 call = reinterpret_cast<CuteQMessageBoxCall35>(taken[35]);
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
      CuteQMessageBoxCall36 call = reinterpret_cast<CuteQMessageBoxCall36>(taken[36]);
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
      CuteQMessageBoxCall37 call = reinterpret_cast<CuteQMessageBoxCall37>(taken[37]);
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
      CuteQMessageBoxCall38 call = reinterpret_cast<CuteQMessageBoxCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQMessageBoxCall39 call = reinterpret_cast<CuteQMessageBoxCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQMessageBoxCall40 call = reinterpret_cast<CuteQMessageBoxCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQMessageBoxCall41 call = reinterpret_cast<CuteQMessageBoxCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQMessageBoxCall42 call = reinterpret_cast<CuteQMessageBoxCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQMessageBoxCall43 call = reinterpret_cast<CuteQMessageBoxCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQMessageBoxCall44 call = reinterpret_cast<CuteQMessageBoxCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQMessageBoxCall45 call = reinterpret_cast<CuteQMessageBoxCall45>(taken[45]);
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
      CuteQMessageBoxCall46 call = reinterpret_cast<CuteQMessageBoxCall46>(taken[46]);
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
      CuteQMessageBoxCall47 call = reinterpret_cast<CuteQMessageBoxCall47>(taken[47]);
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
      CuteQMessageBoxCall48 call = reinterpret_cast<CuteQMessageBoxCall48>(taken[48]);
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
      CuteQMessageBoxCall49 call = reinterpret_cast<CuteQMessageBoxCall49>(taken[49]);
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
      CuteQMessageBoxCall50 call = reinterpret_cast<CuteQMessageBoxCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMessageBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMessageBox10metaObjectEv(
    const QMessageBox *self) {
  return self->metaObject();
}

//  void *QMessageBox::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QMessageBox11qt_metacastEPKc(
    QMessageBox *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMessageBox::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox11qt_metacallEN11QMetaObject4CallEiPPv(
    QMessageBox *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QMessageBox::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QMessageBox2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMessageBox::tr(s, c, n));
}

//  QMessageBox::QMessageBox(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMessageBox *ritual_ZN11QMessageBoxC1EP7QWidget(QWidget *parent) {
  return new CuteQMessageBox(parent);
}

//  QMessageBox::QMessageBox(Icon icon, const QString &title, const QString
//      &text, StandardButtons buttons, QWidget *parent, Qt::WindowFlags
//      flags)
extern "C" Q_DECL_EXPORT
QMessageBox *ritual_ZN11QMessageBoxC1ENS_4IconERK7QStringS3_6QFlagsINS_14StandardButtonEEP7QWidgetS4_IN2Qt10WindowTypeEE(
    QMessageBox::Icon icon,
    const QString *title,
    const QString *text,
    int buttons,
    QWidget *parent,
    int flags) {
  return new CuteQMessageBox(
      icon,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QMessageBox::~QMessageBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBoxD1Ev(QMessageBox *self) {
  delete self;
}

//  void QMessageBox::addButton(QAbstractButton *button, ButtonRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox9addButtonEP15QAbstractButtonNS_10ButtonRoleE(
    QMessageBox *self,
    QAbstractButton *button,
    QMessageBox::ButtonRole role) {
  self->addButton(button, role);
}

//  QPushButton *QMessageBox::addButton(const QString &text, ButtonRole role)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QMessageBox9addButtonERK7QStringNS_10ButtonRoleE(
    QMessageBox *self,
    const QString *text,
    QMessageBox::ButtonRole role) {
  return self->addButton(*text, role);
}

//  QPushButton *QMessageBox::addButton(StandardButton button)
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZN11QMessageBox9addButtonENS_14StandardButtonE(
    QMessageBox *self,
    QMessageBox::StandardButton button) {
  return self->addButton(button);
}

//  void QMessageBox::removeButton(QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox12removeButtonEP15QAbstractButton(
    QMessageBox *self,
    QAbstractButton *button) {
  self->removeButton(button);
}

//  void QMessageBox::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox4openEP7QObjectPKc(
    QMessageBox *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  QList<QAbstractButton *> QMessageBox::buttons() const
extern "C" Q_DECL_EXPORT
QList<QAbstractButton *> *ritual_ZNK11QMessageBox7buttonsEv(
    const QMessageBox *self) {
  return new QList<QAbstractButton *>(self->buttons());
}

//  ButtonRole QMessageBox::buttonRole(QAbstractButton *button) const
extern "C" Q_DECL_EXPORT
QMessageBox::ButtonRole ritual_ZNK11QMessageBox10buttonRoleEP15QAbstractButton(
    const QMessageBox *self,
    QAbstractButton *button) {
  return self->buttonRole(button);
}

//  void QMessageBox::setStandardButtons(StandardButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox18setStandardButtonsE6QFlagsINS_14StandardButtonEE(
    QMessageBox *self,
    int buttons) {
  self->setStandardButtons(
      QFlags<QMessageBox::StandardButton>::fromInt(buttons));
}

//  StandardButtons QMessageBox::standardButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMessageBox15standardButtonsEv(const QMessageBox *self) {
  return static_cast<int>(self->standardButtons().toInt());
}

//  StandardButton QMessageBox::standardButton(QAbstractButton *button) const
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZNK11QMessageBox14standardButtonEP15QAbstractButton(
    const QMessageBox *self,
    QAbstractButton *button) {
  return self->standardButton(button);
}

//  QAbstractButton *QMessageBox::button(StandardButton which) const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK11QMessageBox6buttonENS_14StandardButtonE(
    const QMessageBox *self,
    QMessageBox::StandardButton which) {
  return self->button(which);
}

//  QPushButton *QMessageBox::defaultButton() const
extern "C" Q_DECL_EXPORT
QPushButton *ritual_ZNK11QMessageBox13defaultButtonEv(
    const QMessageBox *self) {
  return self->defaultButton();
}

//  void QMessageBox::setDefaultButton(QPushButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox16setDefaultButtonEP11QPushButton(
    QMessageBox *self,
    QPushButton *button) {
  self->setDefaultButton(button);
}

//  void QMessageBox::setDefaultButton(StandardButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox16setDefaultButtonENS_14StandardButtonE(
    QMessageBox *self,
    QMessageBox::StandardButton button) {
  self->setDefaultButton(button);
}

//  QAbstractButton *QMessageBox::escapeButton() const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK11QMessageBox12escapeButtonEv(
    const QMessageBox *self) {
  return self->escapeButton();
}

//  void QMessageBox::setEscapeButton(QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox15setEscapeButtonEP15QAbstractButton(
    QMessageBox *self,
    QAbstractButton *button) {
  self->setEscapeButton(button);
}

//  void QMessageBox::setEscapeButton(StandardButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox15setEscapeButtonENS_14StandardButtonE(
    QMessageBox *self,
    QMessageBox::StandardButton button) {
  self->setEscapeButton(button);
}

//  QAbstractButton *QMessageBox::clickedButton() const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK11QMessageBox13clickedButtonEv(
    const QMessageBox *self) {
  return self->clickedButton();
}

//  QString QMessageBox::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMessageBox4textEv(const QMessageBox *self) {
  return new QString(self->text());
}

//  void QMessageBox::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox7setTextERK7QString(
    QMessageBox *self,
    const QString *text) {
  self->setText(*text);
}

//  Icon QMessageBox::icon() const
extern "C" Q_DECL_EXPORT
QMessageBox::Icon ritual_ZNK11QMessageBox4iconEv(const QMessageBox *self) {
  return self->icon();
}

//  void QMessageBox::setIcon(Icon a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox7setIconENS_4IconE(
    QMessageBox *self,
    QMessageBox::Icon a0) {
  self->setIcon(a0);
}

//  QPixmap QMessageBox::iconPixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK11QMessageBox10iconPixmapEv(const QMessageBox *self) {
  return new QPixmap(self->iconPixmap());
}

//  void QMessageBox::setIconPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox13setIconPixmapERK7QPixmap(
    QMessageBox *self,
    const QPixmap *pixmap) {
  self->setIconPixmap(*pixmap);
}

//  Qt::TextFormat QMessageBox::textFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK11QMessageBox10textFormatEv(
    const QMessageBox *self) {
  return self->textFormat();
}

//  void QMessageBox::setTextFormat(Qt::TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox13setTextFormatEN2Qt10TextFormatE(
    QMessageBox *self,
    Qt::TextFormat format) {
  self->setTextFormat(format);
}

//  void QMessageBox::setTextInteractionFlags(Qt::TextInteractionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QMessageBox *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QMessageBox::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMessageBox20textInteractionFlagsEv(
    const QMessageBox *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QMessageBox::setCheckBox(QCheckBox *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox11setCheckBoxEP9QCheckBox(
    QMessageBox *self,
    QCheckBox *cb) {
  self->setCheckBox(cb);
}

//  QCheckBox *QMessageBox::checkBox() const
extern "C" Q_DECL_EXPORT
QCheckBox *ritual_ZNK11QMessageBox8checkBoxEv(const QMessageBox *self) {
  return self->checkBox();
}

//  void QMessageBox::setOption(Option option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox9setOptionENS_6OptionEb(
    QMessageBox *self,
    QMessageBox::Option option,
    bool on) {
  self->setOption(option, on);
}

//  bool QMessageBox::testOption(Option option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMessageBox10testOptionENS_6OptionE(
    const QMessageBox *self,
    QMessageBox::Option option) {
  return self->testOption(option);
}

//  void QMessageBox::setOptions(Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox10setOptionsE6QFlagsINS_6OptionEE(
    QMessageBox *self,
    int options) {
  self->setOptions(QFlags<QMessageBox::Option>::fromInt(options));
}

//  Options QMessageBox::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMessageBox7optionsEv(const QMessageBox *self) {
  return static_cast<int>(self->options().toInt());
}

//  StandardButton QMessageBox::information(QWidget *parent, const QString
//      &title, const QString &text, StandardButtons buttons, StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_6QFlagsINS_14StandardButtonEES6_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return QMessageBox::information(
      parent,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  StandardButton QMessageBox::information(QWidget *parent, const QString
//      &title, const QString &text, StandardButton button0, StandardButton
//      button1)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_NS_14StandardButtonES5_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    QMessageBox::StandardButton button0,
    QMessageBox::StandardButton button1) {
  return QMessageBox::information(parent, *title, *text, button0, button1);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  StandardButton QMessageBox::question(QWidget *parent, const QString
//      &title, const QString &text, StandardButtons buttons, StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_6QFlagsINS_14StandardButtonEES6_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return QMessageBox::question(
      parent,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  int QMessageBox::question(QWidget *parent, const QString &title, const
//      QString &text, StandardButton button0, StandardButton button1)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_NS_14StandardButtonES5_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    QMessageBox::StandardButton button0,
    QMessageBox::StandardButton button1) {
  return QMessageBox::question(parent, *title, *text, button0, button1);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  StandardButton QMessageBox::warning(QWidget *parent, const QString
//      &title, const QString &text, StandardButtons buttons, StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_6QFlagsINS_14StandardButtonEES6_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return QMessageBox::warning(
      parent,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  int QMessageBox::warning(QWidget *parent, const QString &title, const
//      QString &text, StandardButton button0, StandardButton button1)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_NS_14StandardButtonES5_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    QMessageBox::StandardButton button0,
    QMessageBox::StandardButton button1) {
  return QMessageBox::warning(parent, *title, *text, button0, button1);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  StandardButton QMessageBox::critical(QWidget *parent, const QString
//      &title, const QString &text, StandardButtons buttons, StandardButton
//      defaultButton)
extern "C" Q_DECL_EXPORT
QMessageBox::StandardButton ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_6QFlagsINS_14StandardButtonEES6_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int buttons,
    QMessageBox::StandardButton defaultButton) {
  return QMessageBox::critical(
      parent,
      *title,
      *text,
      QFlags<QMessageBox::StandardButton>::fromInt(buttons),
      defaultButton);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  int QMessageBox::critical(QWidget *parent, const QString &title, const
//      QString &text, StandardButton button0, StandardButton button1)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_NS_14StandardButtonES5_(
    QWidget *parent,
    const QString *title,
    const QString *text,
    QMessageBox::StandardButton button0,
    QMessageBox::StandardButton button1) {
  return QMessageBox::critical(parent, *title, *text, button0, button1);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QMessageBox::about(QWidget *parent, const QString &title, const
//      QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox5aboutEP7QWidgetRK7QStringS4_(
    QWidget *parent,
    const QString *title,
    const QString *text) {
  QMessageBox::about(parent, *title, *text);
}

//  void QMessageBox::aboutQt(QWidget *parent, const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox7aboutQtEP7QWidgetRK7QString(
    QWidget *parent,
    const QString *title) {
  QMessageBox::aboutQt(parent, *title);
}

#if QT_DEPRECATED_SINCE(6,2)
//  QMessageBox::QMessageBox(const QString &title, const QString &text, Icon
//      icon, int button0, int button1, int button2, QWidget *parent,
//      Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QMessageBox *ritual_ZN11QMessageBoxC1ERK7QStringS2_NS_4IconEiiiP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *title,
    const QString *text,
    QMessageBox::Icon icon,
    int button0,
    int button1,
    int button2,
    QWidget *parent,
    int f) {
  return new CuteQMessageBox(
      *title,
      *text,
      icon,
      button0,
      button1,
      button2,
      parent,
      QFlags<Qt::WindowType>::fromInt(f));
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  int QMessageBox::information(QWidget *parent, const QString &title, const
//      QString &text, int button0, int button1, int button2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_iii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int button0,
    int button1,
    int button2) {
  return QMessageBox::information(
      parent,
      *title,
      *text,
      button0,
      button1,
      button2);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  int QMessageBox::information(QWidget *parent, const QString &title, const
//      QString &text, const QString &button0Text, const QString
//      &button1Text, const QString &button2Text, int defaultButtonNumber,
//      int escapeButtonNumber)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_S4_S4_S4_ii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    const QString *button0Text,
    const QString *button1Text,
    const QString *button2Text,
    int defaultButtonNumber,
    int escapeButtonNumber) {
  return QMessageBox::information(
      parent,
      *title,
      *text,
      *button0Text,
      *button1Text,
      *button2Text,
      defaultButtonNumber,
      escapeButtonNumber);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  int QMessageBox::question(QWidget *parent, const QString &title, const
//      QString &text, int button0, int button1, int button2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_iii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int button0,
    int button1,
    int button2) {
  return QMessageBox::question(
      parent,
      *title,
      *text,
      button0,
      button1,
      button2);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  int QMessageBox::question(QWidget *parent, const QString &title, const
//      QString &text, const QString &button0Text, const QString
//      &button1Text, const QString &button2Text, int defaultButtonNumber,
//      int escapeButtonNumber)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_S4_S4_S4_ii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    const QString *button0Text,
    const QString *button1Text,
    const QString *button2Text,
    int defaultButtonNumber,
    int escapeButtonNumber) {
  return QMessageBox::question(
      parent,
      *title,
      *text,
      *button0Text,
      *button1Text,
      *button2Text,
      defaultButtonNumber,
      escapeButtonNumber);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  int QMessageBox::warning(QWidget *parent, const QString &title, const
//      QString &text, int button0, int button1, int button2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_iii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int button0,
    int button1,
    int button2) {
  return QMessageBox::warning(
      parent,
      *title,
      *text,
      button0,
      button1,
      button2);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  int QMessageBox::warning(QWidget *parent, const QString &title, const
//      QString &text, const QString &button0Text, const QString
//      &button1Text, const QString &button2Text, int defaultButtonNumber,
//      int escapeButtonNumber)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_S4_S4_S4_ii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    const QString *button0Text,
    const QString *button1Text,
    const QString *button2Text,
    int defaultButtonNumber,
    int escapeButtonNumber) {
  return QMessageBox::warning(
      parent,
      *title,
      *text,
      *button0Text,
      *button1Text,
      *button2Text,
      defaultButtonNumber,
      escapeButtonNumber);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  int QMessageBox::critical(QWidget *parent, const QString &title, const
//      QString &text, int button0, int button1, int button2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_iii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    int button0,
    int button1,
    int button2) {
  return QMessageBox::critical(
      parent,
      *title,
      *text,
      button0,
      button1,
      button2);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  int QMessageBox::critical(QWidget *parent, const QString &title, const
//      QString &text, const QString &button0Text, const QString
//      &button1Text, const QString &button2Text, int defaultButtonNumber,
//      int escapeButtonNumber)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_S4_S4_S4_ii(
    QWidget *parent,
    const QString *title,
    const QString *text,
    const QString *button0Text,
    const QString *button1Text,
    const QString *button2Text,
    int defaultButtonNumber,
    int escapeButtonNumber) {
  return QMessageBox::critical(
      parent,
      *title,
      *text,
      *button0Text,
      *button1Text,
      *button2Text,
      defaultButtonNumber,
      escapeButtonNumber);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  QString QMessageBox::buttonText(int button) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMessageBox10buttonTextEi(
    const QMessageBox *self,
    int button) {
  return new QString(self->buttonText(button));
}
#endif  // QT_DEPRECATED_SINCE(6,2)

#if QT_DEPRECATED_SINCE(6,2)
//  void QMessageBox::setButtonText(int button, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox13setButtonTextEiRK7QString(
    QMessageBox *self,
    int button,
    const QString *text) {
  self->setButtonText(button, *text);
}
#endif  // QT_DEPRECATED_SINCE(6,2)

//  QString QMessageBox::informativeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMessageBox15informativeTextEv(
    const QMessageBox *self) {
  return new QString(self->informativeText());
}

//  void QMessageBox::setInformativeText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox18setInformativeTextERK7QString(
    QMessageBox *self,
    const QString *text) {
  self->setInformativeText(*text);
}

#if QT_CONFIG(textedit)
//  QString QMessageBox::detailedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMessageBox12detailedTextEv(const QMessageBox *self) {
  return new QString(self->detailedText());
}
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(textedit)
//  void QMessageBox::setDetailedText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox15setDetailedTextERK7QString(
    QMessageBox *self,
    const QString *text) {
  self->setDetailedText(*text);
}
#endif  // QT_CONFIG(textedit)

//  void QMessageBox::setWindowTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox14setWindowTitleERK7QString(
    QMessageBox *self,
    const QString *title) {
  self->setWindowTitle(*title);
}

//  void QMessageBox::setWindowModality(Qt::WindowModality windowModality)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox17setWindowModalityEN2Qt14WindowModalityE(
    QMessageBox *self,
    Qt::WindowModality windowModality) {
  self->setWindowModality(windowModality);
}

#if QT_DEPRECATED_SINCE(6,2)
//  QPixmap QMessageBox::standardIcon(Icon icon)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN11QMessageBox12standardIconENS_4IconE(
    QMessageBox::Icon icon) {
  return new QPixmap(QMessageBox::standardIcon(icon));
}
#endif  // QT_DEPRECATED_SINCE(6,2)

//  void QMessageBox::buttonClicked(QAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox13buttonClickedEP15QAbstractButton(
    QMessageBox *self,
    QAbstractButton *button) {
  self->buttonClicked(button);
}

//  bool QMessageBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMessageBox5eventEP6QEvent(QMessageBox *self, QEvent *e) {
  return self->event(e);
}

//  void QMessageBox::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox11resizeEventEP12QResizeEvent(
    QMessageBox *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QMessageBox::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox9showEventEP10QShowEvent(
    QMessageBox *self,
    QShowEvent *event) {
  self->showEvent(event);
}

//  void QMessageBox::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox10closeEventEP11QCloseEvent(
    QMessageBox *self,
    QCloseEvent *event) {
  self->closeEvent(event);
}

//  void QMessageBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox13keyPressEventEP9QKeyEvent(
    QMessageBox *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QMessageBox::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMessageBox11changeEventEP6QEvent(
    QMessageBox *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  QMessageBoxPrivate *QMessageBox::d_func()
extern "C" Q_DECL_EXPORT
QMessageBoxPrivate *ritual_ZN11QMessageBox6d_funcEv(QMessageBox *self) {
  return self->d_func();
}

//  const QMessageBoxPrivate *QMessageBox::d_func() const
extern "C" Q_DECL_EXPORT
const QMessageBoxPrivate *ritual_ZNK11QMessageBox6d_funcEv(
    const QMessageBox *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQMessageBox, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMessageBox(
    QMessageBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMessageBox *>(self)->take(key, call);
}

//  bool QMessageBox::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QMessageBox5eventEP6QEvent(
    QMessageBox *self,
    QEvent *e) {
  return static_cast<OwnQMessageBox *>(self)->OwnQMessageBox::event(e);
}

//  void QMessageBox::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QMessageBox11resizeEventEP12QResizeEvent(
    QMessageBox *self,
    QResizeEvent *event) {
  static_cast<OwnQMessageBox *>(self)->OwnQMessageBox::resizeEvent(event);
}

//  void QMessageBox::showEvent(QShowEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QMessageBox9showEventEP10QShowEvent(
    QMessageBox *self,
    QShowEvent *event) {
  static_cast<OwnQMessageBox *>(self)->OwnQMessageBox::showEvent(event);
}

//  void QMessageBox::closeEvent(QCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QMessageBox10closeEventEP11QCloseEvent(
    QMessageBox *self,
    QCloseEvent *event) {
  static_cast<OwnQMessageBox *>(self)->OwnQMessageBox::closeEvent(event);
}

//  void QMessageBox::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QMessageBox13keyPressEventEP9QKeyEvent(
    QMessageBox *self,
    QKeyEvent *event) {
  static_cast<OwnQMessageBox *>(self)->OwnQMessageBox::keyPressEvent(event);
}

//  void QMessageBox::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QMessageBox11changeEventEP6QEvent(
    QMessageBox *self,
    QEvent *event) {
  static_cast<OwnQMessageBox *>(self)->OwnQMessageBox::changeEvent(event);
}

#endif  // QT_CONFIG(messagebox)
#endif  // QT_CONFIG(messagebox)
