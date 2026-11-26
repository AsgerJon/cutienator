//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelega
//  te_p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p_p.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qmimedata.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtQml/QQmlFile>
#include <QtQml/qqmlexpression.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
#include <QtQuick/private/qquicklistview_p.h>
#include <QtQuick/private/qquickitemview_p_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquicksidebar_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquicksidebar_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 190, as _ZN26QQuickFileDialogTapHandlerC1EP10QQuickItem
inline QQuickFileDialogTapHandler::QQuickFileDialogTapHandler(QQuickItem *parent)
    : QQuickTapHandler(parent)
{
    // Set a grab permission that stops the flickable from stealing the drag.
    setGrabPermissions(QQuickPointerHandler::CanTakeOverFromAnything);

    // The drag threshold is used by the handler to know when to start a drag.
    // We handle the drag inpendently, so set the threshold to a big number.
    // This will guarantee that QQuickTapHandler::wantsEventPoint always returns
    // true.
    setDragThreshold(1000);
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 75, as _ZNK31QQuickFileDialogDelegatePrivate14acceptKeyClickEN2Qt3KeyE
inline bool QQuickFileDialogDelegatePrivate::acceptKeyClick(Qt::Key key) const
{
    return key == Qt::Key_Return || key == Qt::Key_Enter;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 25, as _ZN31QQuickFileDialogDelegatePrivate13highlightFileEv
inline void QQuickFileDialogDelegatePrivate::highlightFile()
{
    Q_Q(QQuickFileDialogDelegate);
    QQuickListViewAttached *attached = static_cast<QQuickListViewAttached*>(
        qmlAttachedPropertiesObject<QQuickListView>(q));
    if (!attached)
        return;

    QQmlContext *delegateContext = qmlContext(q);
    if (!delegateContext)
        return;

    bool converted = false;
    const int index = q->property("index").toInt(&converted);
    if (converted) {
        attached->view()->setCurrentIndex(index);
        if (fileDialog)
            fileDialog->setSelectedFile(file);
        else if (folderDialog)
            folderDialog->setSelectedFolder(file);
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 48, as _ZN31QQuickFileDialogDelegatePrivate10chooseFileEv
inline void QQuickFileDialogDelegatePrivate::chooseFile()
{
    const QFileInfo fileInfo(QQmlFile::urlToLocalFileOrQrc(file));
    if (fileInfo.isDir()) {
        // If it's a directory, navigate to it.
        if (fileDialog)
            fileDialog->setCurrentFolder(file);
        else
            folderDialog->setCurrentFolder(file);
    } else {
        Q_ASSERT(fileDialog);
        // Otherwise it's a file, so select it and close the dialog.
        fileDialog->setSelectedFile(file);

        // Prioritize closing the dialog with QQuickDialogPrivate::handleClick() over QQuickDialog::accept()
        const QQuickFileDialogImplAttached *attached = QQuickFileDialogImplPrivate::get(fileDialog)->attachedOrWarn();
        if (Q_LIKELY(attached)) {
            auto *openButton = attached->buttonBox()->standardButton(QPlatformDialogHelper::Open);
            if (Q_LIKELY(openButton)) {
                emit openButton->clicked();
                return;
            }
        }
        fileDialog->accept();
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 173, as _ZN31QQuickFileDialogDelegatePrivate17destroyTapHandlerEv
inline void QQuickFileDialogDelegatePrivate::destroyTapHandler()
{
    if (tapHandler)
        delete tapHandler;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 179, as _ZN31QQuickFileDialogDelegatePrivate15handleLongPressEv
inline void QQuickFileDialogDelegatePrivate::handleLongPress()
{
    if (!tapHandler)
        return;

    tapHandler->m_state = QQuickFileDialogTapHandler::Tracking;
    tapHandler->m_longPressed = true;
}
//  -----------------------------------------------------------------------

//  A QQuickFileDialogDelegatePrivate that Python can take functions over in. Every QQuickFileDialogDelegatePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall0)(const void *, int, int *);
typedef const QPalette * (*CuteQQuickFileDialogDelegatePrivateCall1)(const void *, int *);
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall2)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall3)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall4)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall5)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall6)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall10)(const void *, QQuickItem *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall11)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef void (*CuteQQuickFileDialogDelegatePrivateCall12)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall13)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall14)(const void *, int *);
typedef void * (*CuteQQuickFileDialogDelegatePrivateCall15)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickFileDialogDelegatePrivateCall16)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickFileDialogDelegatePrivateCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickFileDialogDelegatePrivateCall18)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall19)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall20)(const void *, bool, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall21)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall22)(const void *, bool, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall23)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall24)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall25)(const void *, int, int *);
typedef qreal (*CuteQQuickFileDialogDelegatePrivateCall26)(const void *, int *);
typedef qreal (*CuteQQuickFileDialogDelegatePrivateCall27)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall28)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall29)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickFileDialogDelegatePrivateCall30)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall31)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickFileDialogDelegatePrivateCall32)(const void *, int *);
typedef qreal (*CuteQQuickFileDialogDelegatePrivateCall33)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall34)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall35)(const void *, int *);
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall36)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall37)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickFileDialogDelegatePrivateCall38)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickFileDialogDelegatePrivateCall39)(const void *, bool, int *);
typedef void * (*CuteQQuickFileDialogDelegatePrivateCall40)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall41)(const void *, int *);
typedef void (*CuteQQuickFileDialogDelegatePrivateCall42)(const void *, int, int *);
class CuteQQuickFileDialogDelegatePrivate : public QQuickFileDialogDelegatePrivate {
public:
  using QQuickFileDialogDelegatePrivate::QQuickFileDialogDelegatePrivate;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK27QQuickAbstractButtonPrivate14acceptKeyClickEN2Qt3KeyE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate21accessiblePressActionEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QQuickAbstractButtonPrivate22accessibleToggleActionEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[37] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[42] = call;
      return true;
    }
    return false;
  }

  //  bool QQuickFileDialogDelegatePrivate::acceptKeyClick(Qt::Key key)
  //      const
  bool acceptKeyClick(Qt::Key key) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall0 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall0>(taken[0]);
      bool given = call(this, static_cast<int>(key), &handled);
      if (handled) return given;
    }
    return QQuickFileDialogDelegatePrivate::acceptKeyClick(key);
  }

  //  QPalette QQuickItemDelegatePrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall1 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall1>(taken[1]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItemDelegatePrivate::defaultPalette();
  }

  //  bool QQuickAbstractButtonPrivate::handlePress(const QPointF &point,
  //      ulong timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall2 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall2>(taken[2]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickAbstractButtonPrivate::handleMove(const QPointF &point,
  //      ulong timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall3 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall3>(taken[3]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickAbstractButtonPrivate::handleRelease(const QPointF &point,
  //      ulong timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall4 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall4>(taken[4]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickAbstractButtonPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickAbstractButtonPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall5 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::handleUngrab();
  }

  //  void QQuickAbstractButtonPrivate::accessiblePressAction()
  void accessiblePressAction() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall6 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::accessiblePressAction();
  }

  //  void QQuickAbstractButtonPrivate::accessibleToggleAction()
  void accessibleToggleAction() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall7 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::accessibleToggleAction();
  }

  //  void QQuickAbstractButtonPrivate::itemImplicitWidthChanged(QQuickItem
  //      *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall8 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall8>(taken[8]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitWidthChanged(item);
  }

  //  void
  //      QQuickAbstractButtonPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall9 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall9>(taken[9]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickAbstractButtonPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall10 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall10>(taken[10]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickAbstractButtonPrivate::itemDestroyed(item);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall11 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall11>(taken[11]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall12 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall13 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall14 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall15 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall16 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall16>(taken[16]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall17 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall18 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall19 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall20 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall20>(taken[20]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall21 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall22 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall22>(taken[22]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeBackground(complete);
  }

  //  void QQuickControlPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall23 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall23>(taken[23]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall24 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall24>(taken[24]);
      call(this, item, static_cast<int>(reason), &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemFocusChanged(item, reason);
  }

  //  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      a0)
  bool setLastFocusChangeReason(Qt::FocusReason a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall25 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall25>(taken[25]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall26 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall26>(taken[26]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall27 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall27>(taken[27]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall28 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall28>(taken[28]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall29 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall29>(taken[29]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall30 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall30>(taken[30]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall31 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall31>(taken[31]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall32 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall33 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall33>(taken[33]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall34 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall35 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall36 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall36>(taken[36]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall37 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall37>(taken[37]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall38 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall38>(taken[38]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall39 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall39>(taken[39]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall40 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall41 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickFileDialogDelegatePrivateCall42 call = reinterpret_cast<CuteQQuickFileDialogDelegatePrivateCall42>(taken[42]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickFileDialogDelegate *QQuickFileDialogDelegatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFileDialogDelegate *ritual_ZN31QQuickFileDialogDelegatePrivate6q_funcEv(
    QQuickFileDialogDelegatePrivate *self) {
  return self->q_func();
}

//  const QQuickFileDialogDelegate *QQuickFileDialogDelegatePrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickFileDialogDelegate *ritual_ZNK31QQuickFileDialogDelegatePrivate6q_funcEv(
    const QQuickFileDialogDelegatePrivate *self) {
  return self->q_func();
}

//  QQuickFileDialogDelegatePrivate
//      *QQuickFileDialogDelegatePrivate::get(QQuickFileDialogDelegate
//      *delegate)
extern "C" Q_DECL_EXPORT
QQuickFileDialogDelegatePrivate *ritual_ZN31QQuickFileDialogDelegatePrivate3getEP24QQuickFileDialogDelegate(
    QQuickFileDialogDelegate *delegate) {
  return QQuickFileDialogDelegatePrivate::get(delegate);
}

//  void QQuickFileDialogDelegatePrivate::highlightFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickFileDialogDelegatePrivate13highlightFileEv(
    QQuickFileDialogDelegatePrivate *self) {
  self->highlightFile();
}

//  void QQuickFileDialogDelegatePrivate::chooseFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickFileDialogDelegatePrivate10chooseFileEv(
    QQuickFileDialogDelegatePrivate *self) {
  self->chooseFile();
}

//  void QQuickFileDialogDelegatePrivate::destroyTapHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickFileDialogDelegatePrivate17destroyTapHandlerEv(
    QQuickFileDialogDelegatePrivate *self) {
  self->destroyTapHandler();
}

//  void QQuickFileDialogDelegatePrivate::handleLongPress()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickFileDialogDelegatePrivate15handleLongPressEv(
    QQuickFileDialogDelegatePrivate *self) {
  self->handleLongPress();
}

//  bool QQuickFileDialogDelegatePrivate::acceptKeyClick(Qt::Key key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQuickFileDialogDelegatePrivate14acceptKeyClickEN2Qt3KeyE(
    const QQuickFileDialogDelegatePrivate *self,
    Qt::Key key) {
  return self->acceptKeyClick(key);
}

//  a Python function taken by a CuteQQuickFileDialogDelegatePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFileDialogDelegatePrivate(
    QQuickFileDialogDelegatePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFileDialogDelegatePrivate *>(self)->take(key, call);
}

//  bool QQuickFileDialogDelegatePrivate::acceptKeyClick(Qt::Key key) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK31QQuickFileDialogDelegatePrivate14acceptKeyClickEN2Qt3KeyE(
    const QQuickFileDialogDelegatePrivate *self,
    Qt::Key key) {
  return self->QQuickFileDialogDelegatePrivate::acceptKeyClick(key);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
