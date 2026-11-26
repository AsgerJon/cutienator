//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/inlinecomponentutils_p.h>
#include <QtQml/private/qqmlscriptdata_p.h>
#include <QtQml/private/qqmltypenamecache_p.h>
#include <QtQml/private/qv4resolvedtypereference_p.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/qdir.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/qxpfunctional.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/common/qv4compileddata.cpp, line 25, as _ZNK3QV412CompiledData4Unit12verifyHeaderE9QDateTimeP7QString
namespace QV4::CompiledData {
inline bool Unit::verifyHeader(QDateTime expectedSourceTimeStamp, QString *errorString) const
{
    if (strncmp(magic, CompiledData::magic_str, sizeof(magic))) {
        *errorString = QStringLiteral("Magic bytes in the header do not match");
        return false;
    }

    if (version != quint32(QV4_DATA_STRUCTURE_VERSION)) {
        *errorString = QString::fromUtf8("V4 data structure version mismatch. Found %1 expected %2")
                               .arg(quint32(version), 0, 16).arg(QV4_DATA_STRUCTURE_VERSION, 0, 16);
        return false;
    }

    switch (sourceTimeStamp) {
    case 0:
        // No validation necessary
        return true;
    case -1:
        // Content-hash mode: the unit is validated against sourceChecksum rather than the source
        // file's time stamp. The actual comparison is done in CompilationUnit::loadFromDisk, which
        // has access to the source code.
        return true;
    default:
        break;
    }

    // Files from the resource system do not have any time stamps, so fall back to the application
    // executable.
    if (!expectedSourceTimeStamp.isValid()) {
        expectedSourceTimeStamp = QFileInfo(QCoreApplication::applicationFilePath()).lastModified();
        if (!expectedSourceTimeStamp.isValid()) {
            *errorString =
                    QStringLiteral("Failed to get valid timestamp from application executable");
            return false;
        }
    }
    if (expectedSourceTimeStamp.toMSecsSinceEpoch() != sourceTimeStamp) {
        *errorString =
                QStringLiteral("QML source file has a different time stamp than cached file.");
        return false;
    }

    return true;
}
}  // namespace QV4::CompiledData
//  -----------------------------------------------------------------------

//  const QmlUnit *QV4::CompiledData::Unit::qmlUnit() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::QmlUnit *ritual_ZNK3QV412CompiledData4Unit7qmlUnitEv(
    const QV4::CompiledData::Unit *self) {
  return self->qmlUnit();
}

//  QmlUnit *QV4::CompiledData::Unit::qmlUnit()
extern "C" Q_DECL_EXPORT
QV4::CompiledData::QmlUnit *ritual_ZN3QV412CompiledData4Unit7qmlUnitEv(
    QV4::CompiledData::Unit *self) {
  return self->qmlUnit();
}

//  bool QV4::CompiledData::Unit::isSingleton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData4Unit11isSingletonEv(
    const QV4::CompiledData::Unit *self) {
  return self->isSingleton();
}

//  bool QV4::CompiledData::Unit::isListPropertyAssignReplace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData4Unit27isListPropertyAssignReplaceEv(
    const QV4::CompiledData::Unit *self) {
  return self->isListPropertyAssignReplace();
}

//  bool QV4::CompiledData::Unit::isListPropertyAssignReplaceIfNotDefault()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData4Unit39isListPropertyAssignReplaceIfNotDefaultEv(
    const QV4::CompiledData::Unit *self) {
  return self->isListPropertyAssignReplaceIfNotDefault();
}

//  QString QV4::CompiledData::Unit::stringAtInternal(uint idx) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV412CompiledData4Unit16stringAtInternalEj(
    const QV4::CompiledData::Unit *self,
    uint idx) {
  return new QString(self->stringAtInternal(idx));
}

//  const quint32_le *QV4::CompiledData::Unit::functionOffsetTable() const
extern "C" Q_DECL_EXPORT
const quint32_le *ritual_ZNK3QV412CompiledData4Unit19functionOffsetTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->functionOffsetTable();
}

//  const quint32_le *QV4::CompiledData::Unit::classOffsetTable() const
extern "C" Q_DECL_EXPORT
const quint32_le *ritual_ZNK3QV412CompiledData4Unit16classOffsetTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->classOffsetTable();
}

//  const quint32_le *QV4::CompiledData::Unit::templateObjectOffsetTable()
//      const
extern "C" Q_DECL_EXPORT
const quint32_le *ritual_ZNK3QV412CompiledData4Unit25templateObjectOffsetTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->templateObjectOffsetTable();
}

//  const quint32_le *QV4::CompiledData::Unit::blockOffsetTable() const
extern "C" Q_DECL_EXPORT
const quint32_le *ritual_ZNK3QV412CompiledData4Unit16blockOffsetTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->blockOffsetTable();
}

//  const Function *QV4::CompiledData::Unit::functionAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Function *ritual_ZNK3QV412CompiledData4Unit10functionAtEi(
    const QV4::CompiledData::Unit *self,
    int idx) {
  return self->functionAt(idx);
}

//  const Class *QV4::CompiledData::Unit::classAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Class *ritual_ZNK3QV412CompiledData4Unit7classAtEi(
    const QV4::CompiledData::Unit *self,
    int idx) {
  return self->classAt(idx);
}

//  const TemplateObject *QV4::CompiledData::Unit::templateObjectAt(int idx)
//      const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::TemplateObject *ritual_ZNK3QV412CompiledData4Unit16templateObjectAtEi(
    const QV4::CompiledData::Unit *self,
    int idx) {
  return self->templateObjectAt(idx);
}

//  const Block *QV4::CompiledData::Unit::blockAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Block *ritual_ZNK3QV412CompiledData4Unit7blockAtEi(
    const QV4::CompiledData::Unit *self,
    int idx) {
  return self->blockAt(idx);
}

//  const Lookup *QV4::CompiledData::Unit::lookupTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Lookup *ritual_ZNK3QV412CompiledData4Unit11lookupTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->lookupTable();
}

//  const RegExp *QV4::CompiledData::Unit::regexpAt(int index) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::RegExp *ritual_ZNK3QV412CompiledData4Unit8regexpAtEi(
    const QV4::CompiledData::Unit *self,
    int index) {
  return self->regexpAt(index);
}

//  const quint64_le *QV4::CompiledData::Unit::constants() const
extern "C" Q_DECL_EXPORT
const quint64_le *ritual_ZNK3QV412CompiledData4Unit9constantsEv(
    const QV4::CompiledData::Unit *self) {
  return self->constants();
}

//  const JSClassMember *QV4::CompiledData::Unit::jsClassAt(int idx, int
//      *nMembers) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::JSClassMember *ritual_ZNK3QV412CompiledData4Unit9jsClassAtEiPi(
    const QV4::CompiledData::Unit *self,
    int idx,
    int *nMembers) {
  return self->jsClassAt(idx, nMembers);
}

//  const TranslationData *QV4::CompiledData::Unit::translations() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::TranslationData *ritual_ZNK3QV412CompiledData4Unit12translationsEv(
    const QV4::CompiledData::Unit *self) {
  return self->translations();
}

//  const quint32_le *QV4::CompiledData::Unit::translationContextIndex()
//      const
extern "C" Q_DECL_EXPORT
const quint32_le *ritual_ZNK3QV412CompiledData4Unit23translationContextIndexEv(
    const QV4::CompiledData::Unit *self) {
  return self->translationContextIndex();
}

//  quint32_le *QV4::CompiledData::Unit::translationContextIndex()
extern "C" Q_DECL_EXPORT
quint32_le *ritual_ZN3QV412CompiledData4Unit23translationContextIndexEv(
    QV4::CompiledData::Unit *self) {
  return self->translationContextIndex();
}

//  const ImportEntry *QV4::CompiledData::Unit::importEntryTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::ImportEntry *ritual_ZNK3QV412CompiledData4Unit16importEntryTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->importEntryTable();
}

//  const ExportEntry *QV4::CompiledData::Unit::localExportEntryTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::ExportEntry *ritual_ZNK3QV412CompiledData4Unit21localExportEntryTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->localExportEntryTable();
}

//  const ExportEntry *QV4::CompiledData::Unit::indirectExportEntryTable()
//      const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::ExportEntry *ritual_ZNK3QV412CompiledData4Unit24indirectExportEntryTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->indirectExportEntryTable();
}

//  const ExportEntry *QV4::CompiledData::Unit::starExportEntryTable() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::ExportEntry *ritual_ZNK3QV412CompiledData4Unit20starExportEntryTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->starExportEntryTable();
}

//  const quint32_le *QV4::CompiledData::Unit::moduleRequestTable() const
extern "C" Q_DECL_EXPORT
const quint32_le *ritual_ZNK3QV412CompiledData4Unit18moduleRequestTableEv(
    const QV4::CompiledData::Unit *self) {
  return self->moduleRequestTable();
}

//  bool QV4::CompiledData::Unit::verifyHeader(QDateTime
//      expectedSourceTimeStamp, QString *errorString) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData4Unit12verifyHeaderE9QDateTimeP7QString(
    const QV4::CompiledData::Unit *self,
    const QDateTime *expectedSourceTimeStamp,
    QString *errorString) {
  return self->verifyHeader(*expectedSourceTimeStamp, errorString);
}

//  QV4::CompiledData::Unit::~Unit()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData4UnitD1Ev(QV4::CompiledData::Unit *self) {
  delete self;
}
