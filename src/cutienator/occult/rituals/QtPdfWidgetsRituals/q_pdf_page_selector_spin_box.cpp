//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdfWidgets/6.12.0/QtPdfWidgets/private/qpdfpageselector_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtPdfWidgets/QtPdfWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdfWidgets/6.12.0/QtPdfWidgets/private/qpdfpageselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdfWidgets/qpdfpageselector.h>
#include <QtPdfWidgets/private/qpdfpageselector_p.h>
#include <QtPdf/QPdfDocument>
#include <QtWidgets/qboxlayout.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtwebengine/src/pdfwidgets/qpdfpageselector.cpp, line 146, as _ZNK23QPdfPageSelectorSpinBox13valueFromTextERK7QString
inline int QPdfPageSelectorSpinBox::valueFromText(const QString &text) const
{
    if (!m_document)
        return 0;

    return m_document->pageIndexForLabel(text.trimmed());
}

//  from ../qtwebengine/src/pdfwidgets/qpdfpageselector.cpp, line 154, as _ZNK23QPdfPageSelectorSpinBox13textFromValueEi
inline QString QPdfPageSelectorSpinBox::textFromValue(int value) const
{
    if (!m_document)
        return {};

    return m_document->pageLabel(value);
}

//  from ../qtwebengine/src/pdfwidgets/qpdfpageselector.cpp, line 143, as _ZN23QPdfPageSelectorSpinBoxD1Ev
inline QPdfPageSelectorSpinBox::~QPdfPageSelectorSpinBox()
    = default;

//  from ../qtwebengine/src/pdfwidgets/qpdfpageselector.cpp, line 110, as _ZN23QPdfPageSelectorSpinBox21documentStatusChangedEv
inline void QPdfPageSelectorSpinBox::documentStatusChanged()
{
    if (m_document && m_document->status() == QPdfDocument::Status::Ready) {
        setMaximum(m_document->pageCount() - 1);
        setValue(0);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QPdfPageSelectorSpinBox may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPdfPageSelectorSpinBox : QPdfPageSelectorSpinBox {
  using QPdfPageSelectorSpinBox::valueFromText;
  using QPdfPageSelectorSpinBox::textFromValue;
};

//  A QPdfPageSelectorSpinBox that Python can take functions over in. Every QPdfPageSelectorSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(spinbox)
typedef int (*CuteQPdfPageSelectorSpinBoxCall0)(const void *, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQPdfPageSelectorSpinBoxCall1)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef bool (*CuteQPdfPageSelectorSpinBoxCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef const QSize * (*CuteQPdfPageSelectorSpinBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QSize * (*CuteQPdfPageSelectorSpinBoxCall4)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQPdfPageSelectorSpinBoxCall5)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall6)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall8)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall9)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall10)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall11)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall12)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall13)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
#if QT_CONFIG(contextmenu)
typedef void (*CuteQPdfPageSelectorSpinBoxCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(contextmenu)
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall15)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall16)(const void *, QCloseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall17)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall18)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall19)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall20)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall21)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall22)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall23)(const void *, QShowEvent *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQPdfPageSelectorSpinBoxCall24)(const void *, QStyleOptionSpinBox *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef int (*CuteQPdfPageSelectorSpinBoxCall25)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
typedef int (*CuteQPdfPageSelectorSpinBoxCall26)(const void *, int *);
typedef void (*CuteQPdfPageSelectorSpinBoxCall27)(const void *, bool, int *);
typedef int (*CuteQPdfPageSelectorSpinBoxCall28)(const void *, int, int *);
typedef bool (*CuteQPdfPageSelectorSpinBoxCall29)(const void *, int *);
typedef void * (*CuteQPdfPageSelectorSpinBoxCall30)(const void *, int *);
typedef void (*CuteQPdfPageSelectorSpinBoxCall31)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPdfPageSelectorSpinBoxCall32)(const void *, QEnterEvent *, int *);
typedef void (*CuteQPdfPageSelectorSpinBoxCall33)(const void *, QEvent *, int *);
typedef void (*CuteQPdfPageSelectorSpinBoxCall34)(const void *, QMoveEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQPdfPageSelectorSpinBoxCall35)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQPdfPageSelectorSpinBoxCall36)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPdfPageSelectorSpinBoxCall37)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPdfPageSelectorSpinBoxCall38)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPdfPageSelectorSpinBoxCall39)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQPdfPageSelectorSpinBoxCall40)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef int (*CuteQPdfPageSelectorSpinBoxCall41)(const void *, int, int *);
typedef void (*CuteQPdfPageSelectorSpinBoxCall42)(const void *, QPainter *, int *);
typedef void * (*CuteQPdfPageSelectorSpinBoxCall43)(const void *, QPoint *, int *);
typedef void * (*CuteQPdfPageSelectorSpinBoxCall44)(const void *, int *);
typedef void (*CuteQPdfPageSelectorSpinBoxCall45)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQPdfPageSelectorSpinBoxCall46)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfPageSelectorSpinBoxCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageSelectorSpinBoxCall48)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageSelectorSpinBoxCall49)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageSelectorSpinBoxCall50)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfPageSelectorSpinBoxCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPdfPageSelectorSpinBox : public QPdfPageSelectorSpinBox {
public:
  using QPdfPageSelectorSpinBox::QPdfPageSelectorSpinBox;
  void *taken[52] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK8QSpinBox13valueFromTextERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK8QSpinBox13textFromValueEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox6stepByEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN16QAbstractSpinBox5clearEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
#if QT_CONFIG(contextmenu)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(contextmenu)
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox15initStyleOptionEP19QStyleOptionSpinBox")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK16QAbstractSpinBox11stepEnabledEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[34] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
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

#if QT_CONFIG(spinbox)
  //  int QPdfPageSelectorSpinBox::valueFromText(const QString &text) const
  int valueFromText(const QString &text) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall0 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall0>(taken[0]);
      int given = call(this, &text, &handled);
      if (handled) return given;
    }
    return QPdfPageSelectorSpinBox::valueFromText(text);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QString QPdfPageSelectorSpinBox::textFromValue(int value) const
  QString textFromValue(int value) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall1 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall1>(taken[1]);
      QString * given = call(this, value, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPdfPageSelectorSpinBox::textFromValue(value);
  }
#endif  // QT_CONFIG(spinbox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
  //  bool QSpinBox::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall2 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QSpinBox::event(event);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(spinbox)
  //  QSize QAbstractSpinBox::sizeHint() const
  QSize sizeHint() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall3 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::sizeHint();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QSize QAbstractSpinBox::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall4 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::minimumSizeHint();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBox::inputMethodQuery(Qt::InputMethodQuery a0)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall5 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBox::inputMethodQuery(a0);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::stepBy(int steps)
  void stepBy(int steps) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall6 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall6>(taken[6]);
      call(this, steps, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::stepBy(steps);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::clear()
  void clear() override {
    if (taken[7]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall7 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::clear();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall8 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::resizeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall9 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyPressEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall10 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::keyReleaseEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall11 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::wheelEvent(event);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall12 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusInEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall13 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::focusOutEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(spinbox)
#if QT_CONFIG(contextmenu)
  //  void QAbstractSpinBox::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall14 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::contextMenuEvent(event);
  }
#endif  // QT_CONFIG(contextmenu)
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall15 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::changeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall16 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::closeEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall17 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::hideEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall18 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mousePressEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall19 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall20 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall21 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::timerEvent(event);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall22 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::paintEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall23 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::showEvent(event);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBox::initStyleOption(QStyleOptionSpinBox *option)
  //      const
  void initStyleOption(QStyleOptionSpinBox *option) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall24 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall24>(taken[24]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractSpinBox::initStyleOption(option);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  StepEnabled QAbstractSpinBox::stepEnabled() const
  QAbstractSpinBox::StepEnabled stepEnabled() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall25 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QAbstractSpinBox::StepEnabledFlag>::fromInt(given);
    }
    return QAbstractSpinBox::stepEnabled();
  }
#endif  // QT_CONFIG(spinbox)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall26 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[27]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall27 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall27>(taken[27]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall28 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall28>(taken[28]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall29 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall29>(taken[29]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall30 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall31 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall32 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall33 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall34 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall35 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall36 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall37 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall38 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall39 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall40 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall41 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall41>(taken[41]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall42 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall42>(taken[42]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall43 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall43>(taken[43]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall44 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall44>(taken[44]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall45 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[46]) {
      int handled = 0;
      CuteQPdfPageSelectorSpinBoxCall46 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall46>(taken[46]);
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
      CuteQPdfPageSelectorSpinBoxCall47 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall47>(taken[47]);
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
      CuteQPdfPageSelectorSpinBoxCall48 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall48>(taken[48]);
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
      CuteQPdfPageSelectorSpinBoxCall49 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall49>(taken[49]);
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
      CuteQPdfPageSelectorSpinBoxCall50 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall50>(taken[50]);
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
      CuteQPdfPageSelectorSpinBoxCall51 call = reinterpret_cast<CuteQPdfPageSelectorSpinBoxCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPdfPageSelectorSpinBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QPdfPageSelectorSpinBox10metaObjectEv(
    const QPdfPageSelectorSpinBox *self) {
  return self->metaObject();
}

//  void *QPdfPageSelectorSpinBox::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QPdfPageSelectorSpinBox11qt_metacastEPKc(
    QPdfPageSelectorSpinBox *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPdfPageSelectorSpinBox::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QPdfPageSelectorSpinBox11qt_metacallEN11QMetaObject4CallEiPPv(
    QPdfPageSelectorSpinBox *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QPdfPageSelectorSpinBox::~QPdfPageSelectorSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPdfPageSelectorSpinBoxD1Ev(QPdfPageSelectorSpinBox *self) {
  delete self;
}

//  QPdfDocument *QPdfPageSelectorSpinBox::document() const
extern "C" Q_DECL_EXPORT
QPdfDocument *ritual_ZNK23QPdfPageSelectorSpinBox8documentEv(
    const QPdfPageSelectorSpinBox *self) {
  return self->document();
}

//  void QPdfPageSelectorSpinBox::_q_documentChanged(QPdfDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPdfPageSelectorSpinBox18_q_documentChangedEP12QPdfDocument(
    QPdfPageSelectorSpinBox *self,
    QPdfDocument *document) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QPdfPageSelectorSpinBox")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "_q_documentChanged(QPdfDocument *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "_q_documentChanged(QPdfDocument *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&document)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  int QPdfPageSelectorSpinBox::valueFromText(const QString &text) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QPdfPageSelectorSpinBox13valueFromTextERK7QString(
    const QPdfPageSelectorSpinBox *self,
    const QString *text) {
  return self->valueFromText(*text);
}

//  QString QPdfPageSelectorSpinBox::textFromValue(int value) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QPdfPageSelectorSpinBox13textFromValueEi(
    const QPdfPageSelectorSpinBox *self,
    int value) {
  return new QString(self->textFromValue(value));
}

//  QValidator::State QPdfPageSelectorSpinBox::validate(QString &text, int
//      &pos) const
extern "C" Q_DECL_EXPORT
QValidator::State ritual_ZNK23QPdfPageSelectorSpinBox8validateER7QStringRi(
    const QPdfPageSelectorSpinBox *self,
    QString *text,
    int *pos) {
  return self->validate(*text, *pos);
}

//  void QPdfPageSelectorSpinBox::documentStatusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPdfPageSelectorSpinBox21documentStatusChangedEv(
    QPdfPageSelectorSpinBox *self) {
  self->documentStatusChanged();
}

//  a Python function taken by a CuteQPdfPageSelectorSpinBox, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfPageSelectorSpinBox(
    QPdfPageSelectorSpinBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPdfPageSelectorSpinBox *>(self)->take(key, call);
}

//  int QPdfPageSelectorSpinBox::valueFromText(const QString &text) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QPdfPageSelectorSpinBox13valueFromTextERK7QString(
    const QPdfPageSelectorSpinBox *self,
    const QString *text) {
  return static_cast<const OwnQPdfPageSelectorSpinBox *>(self)->OwnQPdfPageSelectorSpinBox::valueFromText(
      *text);
}

//  QString QPdfPageSelectorSpinBox::textFromValue(int value) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK23QPdfPageSelectorSpinBox13textFromValueEi(
    const QPdfPageSelectorSpinBox *self,
    int value) {
  return new QString(
      static_cast<const OwnQPdfPageSelectorSpinBox *>(self)->OwnQPdfPageSelectorSpinBox::textFromValue(
          value));
}
