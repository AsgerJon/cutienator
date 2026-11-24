//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/qprintdialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtPrintSupport/qtprintsupportglobal.h>
#if QT_CONFIG(printdialog)
#if QT_CONFIG(printdialog)
#include <QtPrintSupport/qprintdialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPrintDialog that Python can take functions over in. Every QPrintDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
typedef int (*CuteQPrintDialogCall0)(const void *, int *);
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
#if defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
typedef void (*CuteQPrintDialogCall1)(const void *, int *);
#endif  // defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
typedef void (*CuteQPrintDialogCall2)(const void *, int, int *);
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
#if defined(Q_OS_UNIX) || defined(Q_OS_WIN)
typedef void (*CuteQPrintDialogCall3)(const void *, bool, int *);
#endif  // defined(Q_OS_UNIX) || defined(Q_OS_WIN)
#endif  // QT_CONFIG(printdialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQPrintDialogCall4)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQPrintDialogCall5)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPrintDialogCall6)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPrintDialogCall7)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPrintDialogCall8)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPrintDialogCall9)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPrintDialogCall10)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPrintDialogCall11)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
typedef void (*CuteQPrintDialogCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
typedef bool (*CuteQPrintDialogCall13)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQPrintDialogCall14)(const void *, int *);
typedef int (*CuteQPrintDialogCall15)(const void *, int, int *);
typedef bool (*CuteQPrintDialogCall16)(const void *, int *);
typedef void * (*CuteQPrintDialogCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPrintDialogCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintDialogCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPrintDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPrintDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPrintDialogCall22)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQPrintDialogCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQPrintDialogCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQPrintDialogCall25)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPrintDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPrintDialogCall27)(const void *, QEnterEvent *, int *);
typedef void (*CuteQPrintDialogCall28)(const void *, QEvent *, int *);
typedef void (*CuteQPrintDialogCall29)(const void *, QPaintEvent *, int *);
typedef void (*CuteQPrintDialogCall30)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQPrintDialogCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQPrintDialogCall32)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPrintDialogCall33)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPrintDialogCall34)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPrintDialogCall35)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPrintDialogCall36)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQPrintDialogCall37)(const void *, QHideEvent *, int *);
typedef void (*CuteQPrintDialogCall38)(const void *, QEvent *, int *);
typedef int (*CuteQPrintDialogCall39)(const void *, int, int *);
typedef void (*CuteQPrintDialogCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQPrintDialogCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQPrintDialogCall42)(const void *, int *);
typedef void (*CuteQPrintDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQPrintDialogCall44)(const void *, int, int *);
typedef bool (*CuteQPrintDialogCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintDialogCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintDialogCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintDialogCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintDialogCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPrintDialogCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPrintDialog : public QPrintDialog {
public:
  using QPrintDialog::QPrintDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
#if defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[1] = call;
      return true;
    }
#endif  // defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
#if defined(Q_OS_UNIX) || defined(Q_OS_WIN)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
#endif  // defined(Q_OS_UNIX) || defined(Q_OS_WIN)
#endif  // QT_CONFIG(printdialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6rejectEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[17] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
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
#if QT_CONFIG(printdialog)
  //  int QPrintDialog::exec()
  int exec() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPrintDialogCall0 call = reinterpret_cast<CuteQPrintDialogCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPrintDialog::exec();
  }
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
#if defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
  //  void QPrintDialog::accept()
  void accept() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPrintDialogCall1 call = reinterpret_cast<CuteQPrintDialogCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QPrintDialog::accept();
  }
#endif  // defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(printdialog)
  //  void QPrintDialog::done(int result)
  void done(int result) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPrintDialogCall2 call = reinterpret_cast<CuteQPrintDialogCall2>(taken[2]);
      call(this, result, &handled);
      if (handled) return;
    }
    QPrintDialog::done(result);
  }
#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(printdialog)
#if defined(Q_OS_UNIX) || defined(Q_OS_WIN)
  //  void QPrintDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPrintDialogCall3 call = reinterpret_cast<CuteQPrintDialogCall3>(taken[3]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QPrintDialog::setVisible(visible);
  }
#endif  // defined(Q_OS_UNIX) || defined(Q_OS_WIN)
#endif  // QT_CONFIG(printdialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPrintDialogCall4 call = reinterpret_cast<CuteQPrintDialogCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPrintDialogCall5 call = reinterpret_cast<CuteQPrintDialogCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::open()
  void open() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPrintDialogCall6 call = reinterpret_cast<CuteQPrintDialogCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::reject()
  void reject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQPrintDialogCall7 call = reinterpret_cast<CuteQPrintDialogCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::reject();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPrintDialogCall8 call = reinterpret_cast<CuteQPrintDialogCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::keyPressEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPrintDialogCall9 call = reinterpret_cast<CuteQPrintDialogCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::closeEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPrintDialogCall10 call = reinterpret_cast<CuteQPrintDialogCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::showEvent(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPrintDialogCall11 call = reinterpret_cast<CuteQPrintDialogCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQPrintDialogCall12 call = reinterpret_cast<CuteQPrintDialogCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQPrintDialogCall13 call = reinterpret_cast<CuteQPrintDialogCall13>(taken[13]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QDialog::eventFilter(a0, a1);
  }
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPrintDialogCall14 call = reinterpret_cast<CuteQPrintDialogCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQPrintDialogCall15 call = reinterpret_cast<CuteQPrintDialogCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQPrintDialogCall16 call = reinterpret_cast<CuteQPrintDialogCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPrintDialogCall17 call = reinterpret_cast<CuteQPrintDialogCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPrintDialogCall18 call = reinterpret_cast<CuteQPrintDialogCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPrintDialogCall19 call = reinterpret_cast<CuteQPrintDialogCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPrintDialogCall20 call = reinterpret_cast<CuteQPrintDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPrintDialogCall21 call = reinterpret_cast<CuteQPrintDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPrintDialogCall22 call = reinterpret_cast<CuteQPrintDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQPrintDialogCall23 call = reinterpret_cast<CuteQPrintDialogCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQPrintDialogCall24 call = reinterpret_cast<CuteQPrintDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQPrintDialogCall25 call = reinterpret_cast<CuteQPrintDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQPrintDialogCall26 call = reinterpret_cast<CuteQPrintDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQPrintDialogCall27 call = reinterpret_cast<CuteQPrintDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQPrintDialogCall28 call = reinterpret_cast<CuteQPrintDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQPrintDialogCall29 call = reinterpret_cast<CuteQPrintDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQPrintDialogCall30 call = reinterpret_cast<CuteQPrintDialogCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQPrintDialogCall31 call = reinterpret_cast<CuteQPrintDialogCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQPrintDialogCall32 call = reinterpret_cast<CuteQPrintDialogCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQPrintDialogCall33 call = reinterpret_cast<CuteQPrintDialogCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQPrintDialogCall34 call = reinterpret_cast<CuteQPrintDialogCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQPrintDialogCall35 call = reinterpret_cast<CuteQPrintDialogCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQPrintDialogCall36 call = reinterpret_cast<CuteQPrintDialogCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQPrintDialogCall37 call = reinterpret_cast<CuteQPrintDialogCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQPrintDialogCall38 call = reinterpret_cast<CuteQPrintDialogCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQPrintDialogCall39 call = reinterpret_cast<CuteQPrintDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQPrintDialogCall40 call = reinterpret_cast<CuteQPrintDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQPrintDialogCall41 call = reinterpret_cast<CuteQPrintDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQPrintDialogCall42 call = reinterpret_cast<CuteQPrintDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQPrintDialogCall43 call = reinterpret_cast<CuteQPrintDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQPrintDialogCall44 call = reinterpret_cast<CuteQPrintDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQPrintDialogCall45 call = reinterpret_cast<CuteQPrintDialogCall45>(taken[45]);
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
      CuteQPrintDialogCall46 call = reinterpret_cast<CuteQPrintDialogCall46>(taken[46]);
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
      CuteQPrintDialogCall47 call = reinterpret_cast<CuteQPrintDialogCall47>(taken[47]);
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
      CuteQPrintDialogCall48 call = reinterpret_cast<CuteQPrintDialogCall48>(taken[48]);
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
      CuteQPrintDialogCall49 call = reinterpret_cast<CuteQPrintDialogCall49>(taken[49]);
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
      CuteQPrintDialogCall50 call = reinterpret_cast<CuteQPrintDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPrintDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QPrintDialog10metaObjectEv(
    const QPrintDialog *self) {
  return self->metaObject();
}

//  QString QPrintDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QPrintDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPrintDialog::tr(s, c, n));
}

//  QPrintDialog::QPrintDialog(QPrinter *printer, QWidget *parent)
extern "C" Q_DECL_EXPORT
QPrintDialog *ritual_ZN12QPrintDialogC1EP8QPrinterP7QWidget(
    QPrinter *printer,
    QWidget *parent) {
  return new CuteQPrintDialog(printer, parent);
}

//  QPrintDialog::QPrintDialog(QWidget *parent)
extern "C" Q_DECL_EXPORT
QPrintDialog *ritual_ZN12QPrintDialogC1EP7QWidget(QWidget *parent) {
  return new CuteQPrintDialog(parent);
}

//  QPrintDialog::~QPrintDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintDialogD1Ev(QPrintDialog *self) {
  delete self;
}

//  int QPrintDialog::exec()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QPrintDialog4execEv(QPrintDialog *self) {
  return self->exec();
}

#if defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
//  void QPrintDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintDialog6acceptEv(QPrintDialog *self) {
  self->accept();
}
#endif  // defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)

//  void QPrintDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintDialog4doneEi(QPrintDialog *self, int result) {
  self->done(result);
}

//  void QPrintDialog::setOption(PrintDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintDialog9setOptionEN20QAbstractPrintDialog17PrintDialogOptionEb(
    QPrintDialog *self,
    QAbstractPrintDialog::PrintDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QPrintDialog::testOption(PrintDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDialog10testOptionEN20QAbstractPrintDialog17PrintDialogOptionE(
    const QPrintDialog *self,
    QAbstractPrintDialog::PrintDialogOption option) {
  return self->testOption(option);
}

//  void QPrintDialog::setOptions(PrintDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintDialog10setOptionsE6QFlagsIN20QAbstractPrintDialog17PrintDialogOptionEE(
    QPrintDialog *self,
    int options) {
  self->setOptions(
      QFlags<QAbstractPrintDialog::PrintDialogOption>::fromInt(options));
}

//  PrintDialogOptions QPrintDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPrintDialog7optionsEv(const QPrintDialog *self) {
  return static_cast<int>(self->options().toInt());
}

#if defined(Q_OS_UNIX) || defined(Q_OS_WIN)
//  void QPrintDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintDialog10setVisibleEb(
    QPrintDialog *self,
    bool visible) {
  self->setVisible(visible);
}
#endif  // defined(Q_OS_UNIX) || defined(Q_OS_WIN)

//  void QPrintDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintDialog4openEP7QObjectPKc(
    QPrintDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  a Python function taken by a CuteQPrintDialog, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPrintDialog(
    QPrintDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPrintDialog *>(self)->take(key, call);
}

//  int QPrintDialog::exec()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN12QPrintDialog4execEv(QPrintDialog *self) {
  return self->QPrintDialog::exec();
}

#if defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)
//  void QPrintDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPrintDialog6acceptEv(QPrintDialog *self) {
  self->QPrintDialog::accept();
}
#endif  // defined(Q_OS_UNIX) && !defined(Q_OS_MACOS)

//  void QPrintDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPrintDialog4doneEi(QPrintDialog *self, int result) {
  self->QPrintDialog::done(result);
}

#if defined(Q_OS_UNIX) || defined(Q_OS_WIN)
//  void QPrintDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QPrintDialog10setVisibleEb(
    QPrintDialog *self,
    bool visible) {
  self->QPrintDialog::setVisible(visible);
}
#endif  // defined(Q_OS_UNIX) || defined(Q_OS_WIN)

#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(printdialog)
