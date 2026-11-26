//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmlcompiler_p.h>
#include <QtScxml/private/qscxmlexecutablecontent_p.h>
#include <QtCore/qxmlstream.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qfile.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>
#ifndef BUILD_QSCXMLC
#include <QtScxml/private/qscxmlinvokableservice_p.h>
#include <QtScxml/private/qscxmldatamodel_p.h>
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtScxml/qscxmlstatemachine.h>
#include <QtScxml/private/qscxmltabledata_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#endif
#include <QtCore/qmap.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 2434, as _ZN21QScxmlCompilerPrivate13DefaultLoaderC1Ev
inline QScxmlCompilerPrivate::DefaultLoader::DefaultLoader()
    : Loader()
{}

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 2438, as _ZN21QScxmlCompilerPrivate13DefaultLoader4loadERK7QStringS3_P5QListIS1_E
inline QByteArray QScxmlCompilerPrivate::DefaultLoader::load(const QString &name, const QString &baseDir, QStringList *errors)
{
    QStringList errs;
    QByteArray contents;
#ifdef BUILD_QSCXMLC
    QString cleanName = name;
    if (name.startsWith(QStringLiteral("file:")))
        cleanName = name.mid(5);
    QFileInfo fInfo(cleanName);
#else
    const QUrl url(name);
    if (!url.isLocalFile() && !url.isRelative())
        errs << QStringLiteral("src attribute is not a local file (%1)").arg(name);
    QFileInfo fInfo(url.isLocalFile() ? url.toLocalFile() : name);
#endif // BUILD_QSCXMLC
    if (fInfo.isRelative())
        fInfo = QFileInfo(QDir(baseDir).filePath(fInfo.filePath()));

    if (!fInfo.exists()) {
        errs << QStringLiteral("src attribute resolves to non existing file (%1)").arg(fInfo.filePath());
    } else {
        QFile f(fInfo.filePath());
        if (f.open(QFile::ReadOnly))
            contents = f.readAll();
        else
            errs << QStringLiteral("Failure opening file %1: %2")
                      .arg(fInfo.filePath(), f.errorString());
    }
    if (errors)
        *errors = errs;

    return contents;
}
//  -----------------------------------------------------------------------

//  QScxmlCompilerPrivate::DefaultLoader::DefaultLoader()
extern "C" Q_DECL_EXPORT
QScxmlCompilerPrivate::DefaultLoader *ritual_ZN21QScxmlCompilerPrivate13DefaultLoaderC1Ev() {
  return new QScxmlCompilerPrivate::DefaultLoader();
}

//  QByteArray QScxmlCompilerPrivate::DefaultLoader::load(const QString
//      &name, const QString &baseDir, QStringList *errors)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN21QScxmlCompilerPrivate13DefaultLoader4loadERK7QStringS3_P5QListIS1_E(
    QScxmlCompilerPrivate::DefaultLoader *self,
    const QString *name,
    const QString *baseDir,
    QStringList *errors) {
  return new QByteArray(self->load(*name, *baseDir, errors));
}

//  QScxmlCompilerPrivate::DefaultLoader::~DefaultLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlCompilerPrivate13DefaultLoaderD1Ev(
    QScxmlCompilerPrivate::DefaultLoader *self) {
  delete self;
}
