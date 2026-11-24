//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwareadaptation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwareadaptation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/private/qsgsoftwareinternalrectanglenode_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgsoftwarepainternode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwareglyphnode_p.h>
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarerenderer_p.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/private/qsgsoftwarespritenode_p.h>
#endif
#include <QtCore/QCoreApplication>
#include <QtCore/QElapsedTimer>
#include <QtGui/QWindow>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgsoftwarerenderloop_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtCore/QCoreApplication>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtCore/QElapsedTimer>
#include <QtQuick/private/qquickanimatorcontroller_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQuick/private/qsgsoftwarerenderer_p.h>
#include <QtGui/qpa/qplatformbackingstore.h>
#include <QtGui/QBackingStore>
#include <QtQuick/private/qsgsoftwareadaptation_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/private/qsgsoftwarerenderloop_p.h>
#include <QtQuick/private/qsgsoftwarethreadedrenderloop_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 35, as _ZN18QSGSoftwareContextC1EP7QObject
inline QSGSoftwareContext::QSGSoftwareContext(QObject *parent)
    : QSGContext(parent)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 28, as _ZN21QSGSoftwareRenderLoopC1Ev
inline QSGSoftwareRenderLoop::QSGSoftwareRenderLoop()
{
    sg = new QSGSoftwareContext();
    rc = sg->createRenderContext();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareadaptation.cpp, line 20, as _ZNK21QSGSoftwareAdaptation4keysEv
inline QStringList QSGSoftwareAdaptation::keys() const
{
    return QStringList() << QLatin1String("software") << QLatin1String("softwarecontext");
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareadaptation.cpp, line 25, as _ZNK21QSGSoftwareAdaptation6createERK7QString
inline QSGContext *QSGSoftwareAdaptation::create(const QString &) const
{
    if (!instance)
        instance = new QSGSoftwareContext();
    return instance;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareadaptation.cpp, line 32, as _ZNK21QSGSoftwareAdaptation5flagsERK7QString
inline QSGContextFactoryInterface::Flags QSGSoftwareAdaptation::flags(const QString &) const
{
    // Claim we support adaptable shader effects, then return null for the
    // shader effect node. The result is shader effects not being rendered,
    // with the application working fine in all other respects.
    return QSGContextFactoryInterface::SupportsShaderEffectNode;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareadaptation.cpp, line 40, as _ZN21QSGSoftwareAdaptation19createWindowManagerEv
inline QSGRenderLoop *QSGSoftwareAdaptation::createWindowManager()
{
#if QT_CONFIG(thread)
    static bool threaded = false;
    static bool envChecked = false;
    if (!envChecked) {
        envChecked = true;
        threaded = qgetenv("QSG_RENDER_LOOP") == "threaded";
    }

    if (threaded)
        return new QSGSoftwareThreadedRenderLoop;
#endif

    return new QSGSoftwareRenderLoop();
}
//  -----------------------------------------------------------------------

//  QStringList QSGSoftwareAdaptation::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QSGSoftwareAdaptation4keysEv(
    const QSGSoftwareAdaptation *self) {
  return new QList<QString>(self->keys());
}

//  QSGContext *QSGSoftwareAdaptation::create(const QString &key) const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZNK21QSGSoftwareAdaptation6createERK7QString(
    const QSGSoftwareAdaptation *self,
    const QString *key) {
  return self->create(*key);
}

//  QSGContextFactoryInterface::Flags QSGSoftwareAdaptation::flags(const
//      QString &key) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSGSoftwareAdaptation5flagsERK7QString(
    const QSGSoftwareAdaptation *self,
    const QString *key) {
  return static_cast<int>(self->flags(*key).toInt());
}

//  QSGRenderLoop *QSGSoftwareAdaptation::createWindowManager()
extern "C" Q_DECL_EXPORT
QSGRenderLoop *ritual_ZN21QSGSoftwareAdaptation19createWindowManagerEv(
    QSGSoftwareAdaptation *self) {
  return self->createWindowManager();
}

//  QSGContextFactoryInterface::Flags QSGSoftwareAdaptation::flags(const
//      QString &key) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QSGSoftwareAdaptation5flagsERK7QString(
    const QSGSoftwareAdaptation *self,
    const QString *key) {
  return static_cast<int>(self->QSGSoftwareAdaptation::flags(*key).toInt());
}
