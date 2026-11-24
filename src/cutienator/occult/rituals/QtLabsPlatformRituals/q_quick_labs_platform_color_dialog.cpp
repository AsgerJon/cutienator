//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformcolordialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformcolordialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformdialog_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtLabsPlatform/private/qquicklabsplatformcolordialog_p.h>
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 77, as _ZNK24QQuickLabsPlatformDialog6handleEv
inline QPlatformDialogHelper *QQuickLabsPlatformDialog::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 342, as _ZNK24QQuickLabsPlatformDialog15useNativeDialogEv
inline bool QQuickLabsPlatformDialog::useNativeDialog() const
{
    return !QCoreApplication::testAttribute(Qt::AA_DontUseNativeDialogs)
            && QGuiApplicationPrivate::platformTheme()->usePlatformNativeDialog(m_type);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 122, as _ZNK24QQuickLabsPlatformDialog5titleEv
inline QString QQuickLabsPlatformDialog::title() const
{
    return m_title;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 268, as _ZN24QQuickLabsPlatformDialog6acceptEv
inline void QQuickLabsPlatformDialog::accept()
{
    done(Accepted);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformcolordialog.cpp, line 83, as _ZNK29QQuickLabsPlatformColorDialog5colorEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QColor QQuickLabsPlatformColorDialog::color() const
{
    return m_color;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformcolordialog.cpp, line 109, as _ZNK29QQuickLabsPlatformColorDialog12currentColorEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QColor QQuickLabsPlatformColorDialog::currentColor() const
{
    if (QPlatformColorDialogHelper *colorDialog = qobject_cast<QPlatformColorDialogHelper *>(handle()))
        return colorDialog->currentColor();
    return m_currentColor;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformcolordialog.cpp, line 116, as _ZN29QQuickLabsPlatformColorDialog15setCurrentColorERK6QColor
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformColorDialog::setCurrentColor(const QColor &color)
{
    if (QPlatformColorDialogHelper *colorDialog = qobject_cast<QPlatformColorDialogHelper *>(handle()))
        colorDialog->setCurrentColor(color);
    m_currentColor = color;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformcolordialog.cpp, line 138, as _ZNK29QQuickLabsPlatformColorDialog7optionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QColorDialogOptions::ColorDialogOptions QQuickLabsPlatformColorDialog::options() const
{
    return m_options->options();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformcolordialog.cpp, line 152, as _ZNK29QQuickLabsPlatformColorDialog15useNativeDialogEv
#if QT_DEPRECATED_SINCE(6, 9)
inline bool QQuickLabsPlatformColorDialog::useNativeDialog() const
{
    return QQuickLabsPlatformDialog::useNativeDialog()
            && !m_options->testOption(QColorDialogOptions::DontUseNativeDialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformcolordialog.cpp, line 158, as _ZN29QQuickLabsPlatformColorDialog8onCreateEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformColorDialog::onCreate(QPlatformDialogHelper *dialog)
{
    if (QPlatformColorDialogHelper *colorDialog = qobject_cast<QPlatformColorDialogHelper *>(dialog)) {
        connect(colorDialog, &QPlatformColorDialogHelper::currentColorChanged, this, &QQuickLabsPlatformColorDialog::currentColorChanged);
        colorDialog->setOptions(m_options);
        colorDialog->setCurrentColor(m_currentColor);
    }
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformcolordialog.cpp, line 167, as _ZN29QQuickLabsPlatformColorDialog6onShowEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformColorDialog::onShow(QPlatformDialogHelper *dialog)
{
    m_options->setWindowTitle(title());
    if (QPlatformColorDialogHelper *colorDialog = qobject_cast<QPlatformColorDialogHelper *>(dialog))
        colorDialog->setOptions(m_options);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformcolordialog.cpp, line 174, as _ZN29QQuickLabsPlatformColorDialog6acceptEv
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformColorDialog::accept()
{
    setColor(currentColor());
    QQuickLabsPlatformDialog::accept();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformColorDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformColorDialog : QQuickLabsPlatformColorDialog {
  using QQuickLabsPlatformColorDialog::useNativeDialog;
  using QQuickLabsPlatformColorDialog::onShow;
};

//  const QMetaObject *QQuickLabsPlatformColorDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickLabsPlatformColorDialog10metaObjectEv(
    const QQuickLabsPlatformColorDialog *self) {
  return self->metaObject();
}

//  const QMetaObject *QQuickLabsPlatformColorDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN29QQuickLabsPlatformColorDialog20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformColorDialog::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformColorDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLabsPlatformColorDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformColorDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QColor QQuickLabsPlatformColorDialog::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK29QQuickLabsPlatformColorDialog5colorEv(
    const QQuickLabsPlatformColorDialog *self) {
  return new QColor(self->color());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QColor QQuickLabsPlatformColorDialog::currentColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK29QQuickLabsPlatformColorDialog12currentColorEv(
    const QQuickLabsPlatformColorDialog *self) {
  return new QColor(self->currentColor());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformColorDialog::setCurrentColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLabsPlatformColorDialog15setCurrentColorERK6QColor(
    QQuickLabsPlatformColorDialog *self,
    const QColor *color) {
  self->setCurrentColor(*color);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QColorDialogOptions::ColorDialogOptions
//      QQuickLabsPlatformColorDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickLabsPlatformColorDialog7optionsEv(
    const QQuickLabsPlatformColorDialog *self) {
  return static_cast<int>(self->options().toInt());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  bool QQuickLabsPlatformColorDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickLabsPlatformColorDialog15useNativeDialogEv(
    const QQuickLabsPlatformColorDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickLabsPlatformColorDialog::onCreate(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLabsPlatformColorDialog8onCreateEP21QPlatformDialogHelper(
    QQuickLabsPlatformColorDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickLabsPlatformColorDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLabsPlatformColorDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformColorDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  void QQuickLabsPlatformColorDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickLabsPlatformColorDialog6acceptEv(
    QQuickLabsPlatformColorDialog *self) {
  self->accept();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  bool QQuickLabsPlatformColorDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QQuickLabsPlatformColorDialog15useNativeDialogEv(
    const QQuickLabsPlatformColorDialog *self) {
  return static_cast<const OwnQQuickLabsPlatformColorDialog *>(self)->OwnQQuickLabsPlatformColorDialog::useNativeDialog();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformColorDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickLabsPlatformColorDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformColorDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformColorDialog *>(self)->OwnQQuickLabsPlatformColorDialog::onShow(
      dialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#endif  // QT_DEPRECATED_SINCE(6, 9)
