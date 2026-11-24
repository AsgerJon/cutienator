//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformmessagedialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmessagedialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformdialog_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtLabsPlatform/private/qquicklabsplatformmessagedialog_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtQml/qqmlinfo.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 59, as _ZN24QQuickLabsPlatformDialogC2EN14QPlatformTheme10DialogTypeEP7QObject
inline QQuickLabsPlatformDialog::QQuickLabsPlatformDialog(QPlatformTheme::DialogType type, QObject *parent)
    : QObject(parent),
      m_visible(false),
      m_complete(false),
      m_result(0),
      m_parentWindow(nullptr),
      m_flags(Qt::Dialog),
      m_modality(Qt::WindowModal),
      m_type(type),
      m_handle(nullptr)
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 72, as _ZN24QQuickLabsPlatformDialogD2Ev
inline QQuickLabsPlatformDialog::~QQuickLabsPlatformDialog()
{
    destroy();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 122, as _ZNK24QQuickLabsPlatformDialog5titleEv
inline QString QQuickLabsPlatformDialog::title() const
{
    return m_title;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 212, as _ZNK31QQuickLabsPlatformMessageDialog4textEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformMessageDialog::text() const
{
    return m_options->text();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 235, as _ZNK31QQuickLabsPlatformMessageDialog15informativeTextEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformMessageDialog::informativeText() const
{
    return m_options->informativeText();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 256, as _ZNK31QQuickLabsPlatformMessageDialog12detailedTextEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformMessageDialog::detailedText() const
{
    return m_options->detailedText();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 299, as _ZNK31QQuickLabsPlatformMessageDialog7buttonsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QPlatformDialogHelper::StandardButtons QQuickLabsPlatformMessageDialog::buttons() const
{
    return m_options->standardButtons();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 313, as _ZN31QQuickLabsPlatformMessageDialog8onCreateEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformMessageDialog::onCreate(QPlatformDialogHelper *dialog)
{
    if (QPlatformMessageDialogHelper *messageDialog = qobject_cast<QPlatformMessageDialogHelper *>(dialog)) {
        connect(messageDialog, &QPlatformMessageDialogHelper::clicked, this, &QQuickLabsPlatformMessageDialog::handleClick);
        messageDialog->setOptions(m_options);
    }
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmessagedialog.cpp, line 321, as _ZN31QQuickLabsPlatformMessageDialog6onShowEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformMessageDialog::onShow(QPlatformDialogHelper *dialog)
{
    m_options->setWindowTitle(title());
    if (QPlatformMessageDialogHelper *messageDialog = qobject_cast<QPlatformMessageDialogHelper *>(dialog))
        messageDialog->setOptions(m_options);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformMessageDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformMessageDialog : QQuickLabsPlatformMessageDialog {
  using QQuickLabsPlatformMessageDialog::onShow;
};

//  const QMetaObject *QQuickLabsPlatformMessageDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickLabsPlatformMessageDialog10metaObjectEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return self->metaObject();
}

//  const QMetaObject
//      *QQuickLabsPlatformMessageDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN31QQuickLabsPlatformMessageDialog20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformMessageDialog::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformMessageDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformMessageDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformMessageDialog::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickLabsPlatformMessageDialog4textEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return new QString(self->text());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformMessageDialog::informativeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickLabsPlatformMessageDialog15informativeTextEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return new QString(self->informativeText());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformMessageDialog::detailedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QQuickLabsPlatformMessageDialog12detailedTextEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return new QString(self->detailedText());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QPlatformDialogHelper::StandardButtons
//      QQuickLabsPlatformMessageDialog::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQuickLabsPlatformMessageDialog7buttonsEv(
    const QQuickLabsPlatformMessageDialog *self) {
  return static_cast<int>(self->buttons().toInt());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  void QQuickLabsPlatformMessageDialog::onCreate(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog8onCreateEP21QPlatformDialogHelper(
    QQuickLabsPlatformMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickLabsPlatformMessageDialog::onShow(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMessageDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformMessageDialog::onShow(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQuickLabsPlatformMessageDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformMessageDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformMessageDialog *>(self)->OwnQQuickLabsPlatformMessageDialog::onShow(
      dialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#endif  // QT_DEPRECATED_SINCE(6, 9)
