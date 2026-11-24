//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/plaintexteditor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/plaintexteditor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A qdesigner_internal::PlainTextEditorDialog that Python can take functions over in. Every qdesigner_internal::PlainTextEditorDialog
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*Cuteqdesigner_internal_PlainTextEditorDialogCall1)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef const QSize * (*Cuteqdesigner_internal_PlainTextEditorDialogCall2)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall3)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*Cuteqdesigner_internal_PlainTextEditorDialogCall4)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall5)(const void *, int, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall6)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall7)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall8)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall9)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall10)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall11)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(dialog)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(dialog)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(dialog)
typedef bool (*Cuteqdesigner_internal_PlainTextEditorDialogCall13)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(dialog)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*Cuteqdesigner_internal_PlainTextEditorDialogCall14)(const void *, int *);
typedef int (*Cuteqdesigner_internal_PlainTextEditorDialogCall15)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_PlainTextEditorDialogCall16)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_PlainTextEditorDialogCall17)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_PlainTextEditorDialogCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall19)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall20)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall21)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall22)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall24)(const void *, QKeyEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall25)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall26)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall27)(const void *, QEnterEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall28)(const void *, QEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall29)(const void *, QPaintEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall30)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall32)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall33)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall34)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall35)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall36)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall37)(const void *, QHideEvent *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall38)(const void *, QEvent *, int *);
typedef int (*Cuteqdesigner_internal_PlainTextEditorDialogCall39)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall40)(const void *, QPainter *, int *);
typedef void * (*Cuteqdesigner_internal_PlainTextEditorDialogCall41)(const void *, QPoint *, int *);
typedef void * (*Cuteqdesigner_internal_PlainTextEditorDialogCall42)(const void *, int *);
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall43)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*Cuteqdesigner_internal_PlainTextEditorDialogCall44)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_PlainTextEditorDialogCall45)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall46)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall47)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall49)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_PlainTextEditorDialogCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_PlainTextEditorDialog : public qdesigner_internal::PlainTextEditorDialog {
public:
  using qdesigner_internal::PlainTextEditorDialog::PlainTextEditorDialog;
  void *taken[51] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4openEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4execEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog4doneEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN7QDialog6acceptEv")) {
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
  //  void QDialog::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall0 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDialog::setVisible(visible);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall1 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::sizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  QSize QDialog::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall2 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDialog::minimumSizeHint();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::open()
  void open() override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall3 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::open();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialog::exec()
  int exec() override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall4 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialog::exec();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::done(int a0)
  void done(int a0) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall5 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialog::done(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::accept()
  void accept() override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall6 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDialog::accept();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialog::reject()
  void reject() override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall7 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall7>(taken[7]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall8 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall8>(taken[8]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall9 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall9>(taken[9]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall10 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall10>(taken[10]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall11 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall11>(taken[11]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall12 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall12>(taken[12]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall13 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall13>(taken[13]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall14 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall15 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall16 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall17 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall17>(taken[17]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall18 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall18>(taken[18]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall19 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall20 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall21 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall22 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall22>(taken[22]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall23 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall23>(taken[23]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall24 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall25 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall26 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall27 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall28 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall29 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall30 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall30>(taken[30]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall31 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall31>(taken[31]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall32 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall32>(taken[32]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall33 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall33>(taken[33]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall34 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall34>(taken[34]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall35 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall35>(taken[35]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall36 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall36>(taken[36]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall37 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall38 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[39]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall39 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall39>(taken[39]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[40]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall40 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall40>(taken[40]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[41]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall41 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall41>(taken[41]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[42]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall42 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall42>(taken[42]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall43 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[44]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall44 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall44>(taken[44]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      Cuteqdesigner_internal_PlainTextEditorDialogCall45 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall45>(taken[45]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall46 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall46>(taken[46]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall47 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall47>(taken[47]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall48 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall48>(taken[48]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall49 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall49>(taken[49]);
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
      Cuteqdesigner_internal_PlainTextEditorDialogCall50 call = reinterpret_cast<Cuteqdesigner_internal_PlainTextEditorDialogCall50>(taken[50]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *qdesigner_internal::PlainTextEditorDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal21PlainTextEditorDialog10metaObjectEv(
    const qdesigner_internal::PlainTextEditorDialog *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::PlainTextEditorDialog::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal21PlainTextEditorDialog2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::PlainTextEditorDialog::tr(s, c, n));
}

//  a Python function taken by a
//      Cuteqdesigner_internal_PlainTextEditorDialog, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_PlainTextEditorDialog(
    qdesigner_internal::PlainTextEditorDialog *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_PlainTextEditorDialog *>(self)->take(key, call);
}
