//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfiledialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(filedialog)
#include <QtWidgets/qfiledialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QFileDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFileDialog : QFileDialog {
  using QFileDialog::done;
  using QFileDialog::accept;
  using QFileDialog::changeEvent;
};

//  A QFileDialog that Python can take functions over in. Every QFileDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(filedialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogCall1)(const void *, int, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogCall2)(const void *, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(filedialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQFileDialogCall4)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*CuteQFileDialogCall5)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFileDialogCall6)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQFileDialogCall7)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFileDialogCall8)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFileDialogCall9)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFileDialogCall10)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFileDialogCall11)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFileDialogCall12)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
typedef void (*CuteQFileDialogCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
typedef bool (*CuteQFileDialogCall14)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQFileDialogCall15)(const void *, int *);
typedef int (*CuteQFileDialogCall16)(const void *, int, int *);
typedef bool (*CuteQFileDialogCall17)(const void *, int *);
typedef void * (*CuteQFileDialogCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileDialogCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFileDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFileDialogCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQFileDialogCall23)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQFileDialogCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQFileDialogCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQFileDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*CuteQFileDialogCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQFileDialogCall28)(const void *, QEnterEvent *, int *);
typedef void (*CuteQFileDialogCall29)(const void *, QEvent *, int *);
typedef void (*CuteQFileDialogCall30)(const void *, QPaintEvent *, int *);
typedef void (*CuteQFileDialogCall31)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQFileDialogCall32)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQFileDialogCall33)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFileDialogCall34)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFileDialogCall35)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFileDialogCall36)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQFileDialogCall37)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQFileDialogCall38)(const void *, QHideEvent *, int *);
typedef int (*CuteQFileDialogCall39)(const void *, int, int *);
typedef void (*CuteQFileDialogCall40)(const void *, QPainter *, int *);
typedef void * (*CuteQFileDialogCall41)(const void *, QPoint *, int *);
typedef void * (*CuteQFileDialogCall42)(const void *, int *);
typedef void (*CuteQFileDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQFileDialogCall44)(const void *, int, int *);
typedef bool (*CuteQFileDialogCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDialogCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFileDialog : public QFileDialog {
public:
  using QFileDialog::QFileDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
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
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
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

#if QT_CONFIG(filedialog)
  //  void QFileDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileDialogCall0 call = reinterpret_cast<CuteQFileDialogCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QFileDialog::setVisible(visible);
  }
#endif  // QT_CONFIG(filedialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
  //  void QFileDialog::done(int result)
  void done(int result) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileDialogCall1 call = reinterpret_cast<CuteQFileDialogCall1>(taken[1]);
      call(this, result, &handled);
      if (handled) return;
    }
    QFileDialog::done(result);
  }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
  //  void QFileDialog::accept()
  void accept() override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileDialogCall2 call = reinterpret_cast<CuteQFileDialogCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QFileDialog::accept();
  }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(filedialog)
  //  void QFileDialog::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileDialogCall3 call = reinterpret_cast<CuteQFileDialogCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QFileDialog::changeEvent(e);
  }
#endif  // QT_CONFIG(filedialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileDialogCall4 call = reinterpret_cast<CuteQFileDialogCall4>(taken[4]);
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
      CuteQFileDialogCall5 call = reinterpret_cast<CuteQFileDialogCall5>(taken[5]);
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
      CuteQFileDialogCall6 call = reinterpret_cast<CuteQFileDialogCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialog::exec()
  int exec() override {
    if (taken[7]) {
      int handled = 0;
      CuteQFileDialogCall7 call = reinterpret_cast<CuteQFileDialogCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::reject()
  void reject() override {
    if (taken[8]) {
      int handled = 0;
      CuteQFileDialogCall8 call = reinterpret_cast<CuteQFileDialogCall8>(taken[8]);
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
      CuteQFileDialogCall9 call = reinterpret_cast<CuteQFileDialogCall9>(taken[9]);
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
      CuteQFileDialogCall10 call = reinterpret_cast<CuteQFileDialogCall10>(taken[10]);
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
      CuteQFileDialogCall11 call = reinterpret_cast<CuteQFileDialogCall11>(taken[11]);
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
      CuteQFileDialogCall12 call = reinterpret_cast<CuteQFileDialogCall12>(taken[12]);
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
      CuteQFileDialogCall13 call = reinterpret_cast<CuteQFileDialogCall13>(taken[13]);
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
      CuteQFileDialogCall14 call = reinterpret_cast<CuteQFileDialogCall14>(taken[14]);
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
      CuteQFileDialogCall15 call = reinterpret_cast<CuteQFileDialogCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQFileDialogCall16 call = reinterpret_cast<CuteQFileDialogCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQFileDialogCall17 call = reinterpret_cast<CuteQFileDialogCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQFileDialogCall18 call = reinterpret_cast<CuteQFileDialogCall18>(taken[18]);
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
      CuteQFileDialogCall19 call = reinterpret_cast<CuteQFileDialogCall19>(taken[19]);
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
      CuteQFileDialogCall20 call = reinterpret_cast<CuteQFileDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFileDialogCall21 call = reinterpret_cast<CuteQFileDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFileDialogCall22 call = reinterpret_cast<CuteQFileDialogCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFileDialogCall23 call = reinterpret_cast<CuteQFileDialogCall23>(taken[23]);
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
      CuteQFileDialogCall24 call = reinterpret_cast<CuteQFileDialogCall24>(taken[24]);
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
      CuteQFileDialogCall25 call = reinterpret_cast<CuteQFileDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFileDialogCall26 call = reinterpret_cast<CuteQFileDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQFileDialogCall27 call = reinterpret_cast<CuteQFileDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFileDialogCall28 call = reinterpret_cast<CuteQFileDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFileDialogCall29 call = reinterpret_cast<CuteQFileDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQFileDialogCall30 call = reinterpret_cast<CuteQFileDialogCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQFileDialogCall31 call = reinterpret_cast<CuteQFileDialogCall31>(taken[31]);
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
      CuteQFileDialogCall32 call = reinterpret_cast<CuteQFileDialogCall32>(taken[32]);
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
      CuteQFileDialogCall33 call = reinterpret_cast<CuteQFileDialogCall33>(taken[33]);
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
      CuteQFileDialogCall34 call = reinterpret_cast<CuteQFileDialogCall34>(taken[34]);
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
      CuteQFileDialogCall35 call = reinterpret_cast<CuteQFileDialogCall35>(taken[35]);
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
      CuteQFileDialogCall36 call = reinterpret_cast<CuteQFileDialogCall36>(taken[36]);
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
      CuteQFileDialogCall37 call = reinterpret_cast<CuteQFileDialogCall37>(taken[37]);
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
      CuteQFileDialogCall38 call = reinterpret_cast<CuteQFileDialogCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFileDialogCall39 call = reinterpret_cast<CuteQFileDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQFileDialogCall40 call = reinterpret_cast<CuteQFileDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQFileDialogCall41 call = reinterpret_cast<CuteQFileDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQFileDialogCall42 call = reinterpret_cast<CuteQFileDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQFileDialogCall43 call = reinterpret_cast<CuteQFileDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQFileDialogCall44 call = reinterpret_cast<CuteQFileDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQFileDialogCall45 call = reinterpret_cast<CuteQFileDialogCall45>(taken[45]);
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
      CuteQFileDialogCall46 call = reinterpret_cast<CuteQFileDialogCall46>(taken[46]);
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
      CuteQFileDialogCall47 call = reinterpret_cast<CuteQFileDialogCall47>(taken[47]);
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
      CuteQFileDialogCall48 call = reinterpret_cast<CuteQFileDialogCall48>(taken[48]);
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
      CuteQFileDialogCall49 call = reinterpret_cast<CuteQFileDialogCall49>(taken[49]);
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
      CuteQFileDialogCall50 call = reinterpret_cast<CuteQFileDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFileDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFileDialog10metaObjectEv(
    const QFileDialog *self) {
  return self->metaObject();
}

//  QString QFileDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileDialog::tr(s, c, n));
}

//  QFileDialog::QFileDialog(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QFileDialog *ritual_ZN11QFileDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQFileDialog(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QFileDialog::QFileDialog(QWidget *parent, const QString &caption, const
//      QString &directory, const QString &filter)
extern "C" Q_DECL_EXPORT
QFileDialog *ritual_ZN11QFileDialogC1EP7QWidgetRK7QStringS4_S4_(
    QWidget *parent,
    const QString *caption,
    const QString *directory,
    const QString *filter) {
  return new CuteQFileDialog(parent, *caption, *directory, *filter);
}

//  QFileDialog::~QFileDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialogD1Ev(QFileDialog *self) {
  delete self;
}

//  void QFileDialog::setDirectory(const QString &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog12setDirectoryERK7QString(
    QFileDialog *self,
    const QString *directory) {
  self->setDirectory(*directory);
}

//  void QFileDialog::setDirectory(const QDir &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog12setDirectoryERK4QDir(
    QFileDialog *self,
    const QDir *directory) {
  self->setDirectory(*directory);
}

//  QDir QFileDialog::directory() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK11QFileDialog9directoryEv(const QFileDialog *self) {
  return new QDir(self->directory());
}

//  void QFileDialog::setDirectoryUrl(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog15setDirectoryUrlERK4QUrl(
    QFileDialog *self,
    const QUrl *directory) {
  self->setDirectoryUrl(*directory);
}

//  QUrl QFileDialog::directoryUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK11QFileDialog12directoryUrlEv(const QFileDialog *self) {
  return new QUrl(self->directoryUrl());
}

//  void QFileDialog::selectFile(const QString &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog10selectFileERK7QString(
    QFileDialog *self,
    const QString *filename) {
  self->selectFile(*filename);
}

//  QStringList QFileDialog::selectedFiles() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QFileDialog13selectedFilesEv(
    const QFileDialog *self) {
  return new QList<QString>(self->selectedFiles());
}

//  void QFileDialog::selectUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog9selectUrlERK4QUrl(
    QFileDialog *self,
    const QUrl *url) {
  self->selectUrl(*url);
}

//  QList<QUrl> QFileDialog::selectedUrls() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK11QFileDialog12selectedUrlsEv(
    const QFileDialog *self) {
  return new QList<QUrl>(self->selectedUrls());
}

//  void QFileDialog::setNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog13setNameFilterERK7QString(
    QFileDialog *self,
    const QString *filter) {
  self->setNameFilter(*filter);
}

//  void QFileDialog::setNameFilters(const QStringList &filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog14setNameFiltersERK5QListI7QStringE(
    QFileDialog *self,
    const QList<QString> *filters) {
  self->setNameFilters(*filters);
}

//  QStringList QFileDialog::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QFileDialog11nameFiltersEv(
    const QFileDialog *self) {
  return new QList<QString>(self->nameFilters());
}

//  void QFileDialog::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog16selectNameFilterERK7QString(
    QFileDialog *self,
    const QString *filter) {
  self->selectNameFilter(*filter);
}

//  QString QFileDialog::selectedMimeTypeFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDialog22selectedMimeTypeFilterEv(
    const QFileDialog *self) {
  return new QString(self->selectedMimeTypeFilter());
}

//  QString QFileDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDialog18selectedNameFilterEv(
    const QFileDialog *self) {
  return new QString(self->selectedNameFilter());
}

#if QT_CONFIG(mimetype)
//  void QFileDialog::setMimeTypeFilters(const QStringList &filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog18setMimeTypeFiltersERK5QListI7QStringE(
    QFileDialog *self,
    const QList<QString> *filters) {
  self->setMimeTypeFilters(*filters);
}
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
//  QStringList QFileDialog::mimeTypeFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QFileDialog15mimeTypeFiltersEv(
    const QFileDialog *self) {
  return new QList<QString>(self->mimeTypeFilters());
}
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
//  void QFileDialog::selectMimeTypeFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog20selectMimeTypeFilterERK7QString(
    QFileDialog *self,
    const QString *filter) {
  self->selectMimeTypeFilter(*filter);
}
#endif  // QT_CONFIG(mimetype)

//  QDir::Filters QFileDialog::filter() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFileDialog6filterEv(const QFileDialog *self) {
  return static_cast<int>(self->filter().toInt());
}

//  void QFileDialog::setFilter(QDir::Filters filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog9setFilterE6QFlagsIN4QDir6FilterEE(
    QFileDialog *self,
    int filters) {
  self->setFilter(QFlags<QDir::Filter>::fromInt(filters));
}

//  void QFileDialog::setViewMode(ViewMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog11setViewModeENS_8ViewModeE(
    QFileDialog *self,
    QFileDialog::ViewMode mode) {
  self->setViewMode(mode);
}

//  ViewMode QFileDialog::viewMode() const
extern "C" Q_DECL_EXPORT
QFileDialog::ViewMode ritual_ZNK11QFileDialog8viewModeEv(
    const QFileDialog *self) {
  return self->viewMode();
}

//  void QFileDialog::setFileMode(FileMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog11setFileModeENS_8FileModeE(
    QFileDialog *self,
    QFileDialog::FileMode mode) {
  self->setFileMode(mode);
}

//  FileMode QFileDialog::fileMode() const
extern "C" Q_DECL_EXPORT
QFileDialog::FileMode ritual_ZNK11QFileDialog8fileModeEv(
    const QFileDialog *self) {
  return self->fileMode();
}

//  void QFileDialog::setAcceptMode(AcceptMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog13setAcceptModeENS_10AcceptModeE(
    QFileDialog *self,
    QFileDialog::AcceptMode mode) {
  self->setAcceptMode(mode);
}

//  AcceptMode QFileDialog::acceptMode() const
extern "C" Q_DECL_EXPORT
QFileDialog::AcceptMode ritual_ZNK11QFileDialog10acceptModeEv(
    const QFileDialog *self) {
  return self->acceptMode();
}

//  void QFileDialog::setSidebarUrls(const QList<QUrl> &urls)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog14setSidebarUrlsERK5QListI4QUrlE(
    QFileDialog *self,
    const QList<QUrl> *urls) {
  self->setSidebarUrls(*urls);
}

//  QList<QUrl> QFileDialog::sidebarUrls() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK11QFileDialog11sidebarUrlsEv(
    const QFileDialog *self) {
  return new QList<QUrl>(self->sidebarUrls());
}

//  QByteArray QFileDialog::saveState() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QFileDialog9saveStateEv(const QFileDialog *self) {
  return new QByteArray(self->saveState());
}

//  bool QFileDialog::restoreState(const QByteArray &state)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDialog12restoreStateERK10QByteArray(
    QFileDialog *self,
    const QByteArray *state) {
  return self->restoreState(*state);
}

//  void QFileDialog::setDefaultSuffix(const QString &suffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog16setDefaultSuffixERK7QString(
    QFileDialog *self,
    const QString *suffix) {
  self->setDefaultSuffix(*suffix);
}

//  QString QFileDialog::defaultSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDialog13defaultSuffixEv(const QFileDialog *self) {
  return new QString(self->defaultSuffix());
}

//  void QFileDialog::setHistory(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog10setHistoryERK5QListI7QStringE(
    QFileDialog *self,
    const QList<QString> *paths) {
  self->setHistory(*paths);
}

//  QStringList QFileDialog::history() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QFileDialog7historyEv(const QFileDialog *self) {
  return new QList<QString>(self->history());
}

//  void QFileDialog::setItemDelegate(QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog15setItemDelegateEP21QAbstractItemDelegate(
    QFileDialog *self,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegate(delegate);
}

//  QAbstractItemDelegate *QFileDialog::itemDelegate() const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK11QFileDialog12itemDelegateEv(
    const QFileDialog *self) {
  return self->itemDelegate();
}

//  void QFileDialog::setIconProvider(QAbstractFileIconProvider *provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog15setIconProviderEP25QAbstractFileIconProvider(
    QFileDialog *self,
    QAbstractFileIconProvider *provider) {
  self->setIconProvider(provider);
}

//  QAbstractFileIconProvider *QFileDialog::iconProvider() const
extern "C" Q_DECL_EXPORT
QAbstractFileIconProvider *ritual_ZNK11QFileDialog12iconProviderEv(
    const QFileDialog *self) {
  return self->iconProvider();
}

//  void QFileDialog::setLabelText(DialogLabel label, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog12setLabelTextENS_11DialogLabelERK7QString(
    QFileDialog *self,
    QFileDialog::DialogLabel label,
    const QString *text) {
  self->setLabelText(label, *text);
}

//  QString QFileDialog::labelText(DialogLabel label) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDialog9labelTextENS_11DialogLabelE(
    const QFileDialog *self,
    QFileDialog::DialogLabel label) {
  return new QString(self->labelText(label));
}

//  void QFileDialog::setSupportedSchemes(const QStringList &schemes)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog19setSupportedSchemesERK5QListI7QStringE(
    QFileDialog *self,
    const QList<QString> *schemes) {
  self->setSupportedSchemes(*schemes);
}

//  QStringList QFileDialog::supportedSchemes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QFileDialog16supportedSchemesEv(
    const QFileDialog *self) {
  return new QList<QString>(self->supportedSchemes());
}

#if QT_CONFIG(proxymodel)
//  void QFileDialog::setProxyModel(QAbstractProxyModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog13setProxyModelEP19QAbstractProxyModel(
    QFileDialog *self,
    QAbstractProxyModel *model) {
  self->setProxyModel(model);
}
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
//  QAbstractProxyModel *QFileDialog::proxyModel() const
extern "C" Q_DECL_EXPORT
QAbstractProxyModel *ritual_ZNK11QFileDialog10proxyModelEv(
    const QFileDialog *self) {
  return self->proxyModel();
}
#endif  // QT_CONFIG(proxymodel)

//  void QFileDialog::setOption(Option option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog9setOptionENS_6OptionEb(
    QFileDialog *self,
    QFileDialog::Option option,
    bool on) {
  self->setOption(option, on);
}

//  bool QFileDialog::testOption(Option option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFileDialog10testOptionENS_6OptionE(
    const QFileDialog *self,
    QFileDialog::Option option) {
  return self->testOption(option);
}

//  void QFileDialog::setOptions(Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog10setOptionsE6QFlagsINS_6OptionEE(
    QFileDialog *self,
    int options) {
  self->setOptions(QFlags<QFileDialog::Option>::fromInt(options));
}

//  Options QFileDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFileDialog7optionsEv(const QFileDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QFileDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog4openEP7QObjectPKc(
    QFileDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  void QFileDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog10setVisibleEb(QFileDialog *self, bool visible) {
  self->setVisible(visible);
}

//  QString QFileDialog::getOpenFileName(QWidget *parent, const QString
//      &caption, const QString &dir, const QString &filter, QString
//      *selectedFilter, Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDialog15getOpenFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsINS_6OptionEE(
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      QFileDialog::getOpenFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QUrl QFileDialog::getOpenFileUrl(QWidget *parent, const QString &caption,
//      const QUrl &dir, const QString &filter, QString *selectedFilter,
//      Options options, const QStringList &supportedSchemes)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN11QFileDialog14getOpenFileUrlEP7QWidgetRK7QStringRK4QUrlS4_PS2_6QFlagsINS_6OptionEERK5QListIS2_E(
    QWidget *parent,
    const QString *caption,
    const QUrl *dir,
    const QString *filter,
    QString *selectedFilter,
    int options,
    const QList<QString> *supportedSchemes) {
  return new QUrl(
      QFileDialog::getOpenFileUrl(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options),
          *supportedSchemes));
}

//  QString QFileDialog::getSaveFileName(QWidget *parent, const QString
//      &caption, const QString &dir, const QString &filter, QString
//      *selectedFilter, Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDialog15getSaveFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsINS_6OptionEE(
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      QFileDialog::getSaveFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QUrl QFileDialog::getSaveFileUrl(QWidget *parent, const QString &caption,
//      const QUrl &dir, const QString &filter, QString *selectedFilter,
//      Options options, const QStringList &supportedSchemes)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN11QFileDialog14getSaveFileUrlEP7QWidgetRK7QStringRK4QUrlS4_PS2_6QFlagsINS_6OptionEERK5QListIS2_E(
    QWidget *parent,
    const QString *caption,
    const QUrl *dir,
    const QString *filter,
    QString *selectedFilter,
    int options,
    const QList<QString> *supportedSchemes) {
  return new QUrl(
      QFileDialog::getSaveFileUrl(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options),
          *supportedSchemes));
}

//  QString QFileDialog::getExistingDirectory(QWidget *parent, const QString
//      &caption, const QString &dir, Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDialog20getExistingDirectoryEP7QWidgetRK7QStringS4_6QFlagsINS_6OptionEE(
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    int options) {
  return new QString(
      QFileDialog::getExistingDirectory(
          parent,
          *caption,
          *dir,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QUrl QFileDialog::getExistingDirectoryUrl(QWidget *parent, const QString
//      &caption, const QUrl &dir, Options options, const QStringList
//      &supportedSchemes)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN11QFileDialog23getExistingDirectoryUrlEP7QWidgetRK7QStringRK4QUrl6QFlagsINS_6OptionEERK5QListIS2_E(
    QWidget *parent,
    const QString *caption,
    const QUrl *dir,
    int options,
    const QList<QString> *supportedSchemes) {
  return new QUrl(
      QFileDialog::getExistingDirectoryUrl(
          parent,
          *caption,
          *dir,
          QFlags<QFileDialog::Option>::fromInt(options),
          *supportedSchemes));
}

//  QStringList QFileDialog::getOpenFileNames(QWidget *parent, const QString
//      &caption, const QString &dir, const QString &filter, QString
//      *selectedFilter, Options options)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN11QFileDialog16getOpenFileNamesEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsINS_6OptionEE(
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QList<QString>(
      QFileDialog::getOpenFileNames(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QList<QUrl> QFileDialog::getOpenFileUrls(QWidget *parent, const QString
//      &caption, const QUrl &dir, const QString &filter, QString
//      *selectedFilter, Options options, const QStringList
//      &supportedSchemes)
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZN11QFileDialog15getOpenFileUrlsEP7QWidgetRK7QStringRK4QUrlS4_PS2_6QFlagsINS_6OptionEERK5QListIS2_E(
    QWidget *parent,
    const QString *caption,
    const QUrl *dir,
    const QString *filter,
    QString *selectedFilter,
    int options,
    const QList<QString> *supportedSchemes) {
  return new QList<QUrl>(
      QFileDialog::getOpenFileUrls(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options),
          *supportedSchemes));
}

//  void QFileDialog::saveFileContent(const QByteArray &fileContent, const
//      QString &fileNameHint, QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog15saveFileContentERK10QByteArrayRK7QStringP7QWidget(
    const QByteArray *fileContent,
    const QString *fileNameHint,
    QWidget *parent) {
  QFileDialog::saveFileContent(*fileContent, *fileNameHint, parent);
}

//  QFileDialog::QFileDialog(const QFileDialogArgs &args)
extern "C" Q_DECL_EXPORT
QFileDialog *ritual_ZN11QFileDialogC1ERK15QFileDialogArgs(
    const QFileDialogArgs *args) {
  return new CuteQFileDialog(*args);
}

//  void QFileDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog4doneEi(QFileDialog *self, int result) {
  self->done(result);
}

//  void QFileDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog6acceptEv(QFileDialog *self) {
  self->accept();
}

//  void QFileDialog::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog11changeEventEP6QEvent(
    QFileDialog *self,
    QEvent *e) {
  self->changeEvent(e);
}

//  QFileDialogPrivate *QFileDialog::d_func()
extern "C" Q_DECL_EXPORT
QFileDialogPrivate *ritual_ZN11QFileDialog6d_funcEv(QFileDialog *self) {
  return self->d_func();
}

//  const QFileDialogPrivate *QFileDialog::d_func() const
extern "C" Q_DECL_EXPORT
const QFileDialogPrivate *ritual_ZNK11QFileDialog6d_funcEv(
    const QFileDialog *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQFileDialog, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileDialog(
    QFileDialog *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileDialog *>(self)->take(key, call);
}

//  void QFileDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFileDialog10setVisibleEb(
    QFileDialog *self,
    bool visible) {
  self->QFileDialog::setVisible(visible);
}

//  void QFileDialog::done(int result)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFileDialog4doneEi(QFileDialog *self, int result) {
  static_cast<OwnQFileDialog *>(self)->OwnQFileDialog::done(result);
}

//  void QFileDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFileDialog6acceptEv(QFileDialog *self) {
  static_cast<OwnQFileDialog *>(self)->OwnQFileDialog::accept();
}

//  void QFileDialog::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFileDialog11changeEventEP6QEvent(
    QFileDialog *self,
    QEvent *e) {
  static_cast<OwnQFileDialog *>(self)->OwnQFileDialog::changeEvent(e);
}

#endif  // QT_CONFIG(filedialog)
