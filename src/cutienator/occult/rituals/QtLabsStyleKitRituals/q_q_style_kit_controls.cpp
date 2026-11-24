//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrols_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qobject.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 654, as _ZNK18QQStyleKitControls15getControlStyleEj
inline QQStyleKitControl* QQStyleKitControls::getControlStyle(QQStyleKitExtendableControlType controlType) const
{
    return m_controls.value(controlType, nullptr);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 614, as _ZNK18QQStyleKitControls8childrenEv
inline const QList<QObject *> QQStyleKitControls::children() const
{
    return m_data;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 725, as _ZN18QQStyleKitControls17componentCompleteEv
inline void QQStyleKitControls::componentComplete()
{
    for (auto *obj : children()) {
        if (auto *customControl = qobject_cast<QQStyleKitCustomControl *>(obj)) {
            const QQStyleKitExtendableControlType type = customControl->controlType();
            const QQStyleKitExtendableControlType reserved
                = QQStyleKitExtendableControlType(QQStyleKitReader::ControlType::Unspecified);
            if (type >= reserved)
                qmlWarning(this) << "CustomControls must use a controlType less than " << reserved;
            if (m_controls.contains(type))
                qmlWarning(this) << "CustomControl registered more than once: " << type;
            m_controls.insert(type, customControl);
        }
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQStyleKitControls may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQStyleKitControls : QQStyleKitControls {
  using QQStyleKitControls::classBegin;
};

//  const QMetaObject *QQStyleKitControls::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQStyleKitControls10metaObjectEv(
    const QQStyleKitControls *self) {
  return self->metaObject();
}

//  void QQStyleKitControls::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls24qt_qmlMarker_uncreatableEv(
    QQStyleKitControls *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQStyleKitControl
//      *QQStyleKitControls::getControlStyle(QQStyleKitExtendableControlType
//      controlType) const
extern "C" Q_DECL_EXPORT
QQStyleKitControl *ritual_ZNK18QQStyleKitControls15getControlStyleEj(
    const QQStyleKitControls *self,
    QQStyleKitExtendableControlType controlType) {
  return self->getControlStyle(controlType);
}

//  const QList<QObject *> QQStyleKitControls::children() const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK18QQStyleKitControls8childrenEv(
    const QQStyleKitControls *self) {
  return new QList<QObject *>(self->children());
}

//  void QQStyleKitControls::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls10classBeginEv(QQStyleKitControls *self) {
  self->classBegin();
}

//  void QQStyleKitControls::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitControls17componentCompleteEv(
    QQStyleKitControls *self) {
  self->componentComplete();
}

//  QQStyleKitControls as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQStyleKitControls_QQmlParserStatus(
    QQStyleKitControls *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QQStyleKitControls::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQStyleKitControls10classBeginEv(
    QQStyleKitControls *self) {
  static_cast<OwnQQStyleKitControls *>(self)->OwnQQStyleKitControls::classBegin();
}
