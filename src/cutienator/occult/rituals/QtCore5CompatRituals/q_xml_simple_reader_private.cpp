//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qxml_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/qxml.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qxml_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qxml.h"
#include "qxml_p.h"
#if QT_CONFIG(textcodec)
#include "qtextcodec.h"
#endif
#include "qbuffer.h"
#if QT_CONFIG(regularexpression)
#include "qregularexpression.h"
#endif
#include "qmap.h"
#include "qhash.h"
#include "qstack.h"
#include <QtCore/qvarlengtharray.h>
#include <qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2461, as _ZN23QXmlSimpleReaderPrivateD1Ev
inline QXmlSimpleReaderPrivate::~QXmlSimpleReaderPrivate()
{
    delete parseStack;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2466, as _ZN23QXmlSimpleReaderPrivate22initIncrementalParsingEv
inline void QXmlSimpleReaderPrivate::initIncrementalParsing()
{
    if (parseStack)
        parseStack->clear();
    else
        parseStack = new QStack<ParseState>;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2427, as _ZN23QXmlSimpleReaderPrivate11stringClearEv
inline void QXmlSimpleReaderPrivate::stringClear()
{
    stringValueLen = 0; stringArrayPos = 0;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2431, as _ZN23QXmlSimpleReaderPrivate9nameClearEv
inline void QXmlSimpleReaderPrivate::nameClear()
{
    nameValueLen = 0; nameArrayPos = 0;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2436, as _ZN23QXmlSimpleReaderPrivate8refClearEv
inline void QXmlSimpleReaderPrivate::refClear()
{
    refValueLen = 0; refArrayPos = 0;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7511, as _ZN23QXmlSimpleReaderPrivate4nextEv
inline void QXmlSimpleReaderPrivate::next()
{
    int count = xmlRefStack.size();
    while (count != 0) {
        if (xmlRefStack.top().isEmpty()) {
            xmlRefStack.pop_back();
            count--;
        } else {
            c = xmlRefStack.top().next();
            return;
        }
    }

    // the following could be written nicer, but since it is a time-critical
    // function, rather optimize for speed
    ushort uc = c.unicode();
    c = inputSource->next();
    // If we are not incremental parsing, we just skip over EndOfData chars to give the
    // parser an uninterrupted stream of document chars.
    if (c == QXmlInputSource::EndOfData && parseStack == nullptr)
        c = inputSource->next();
    if (uc == '\n') {
        lineNr++;
        columnNr = -1;
    } else if (uc == '\r') {
        if (c != QLatin1Char('\n')) {
            lineNr++;
            columnNr = -1;
        }
    }
    ++columnNr;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 2422, as _ZN23QXmlSimpleReaderPrivate5atEndEv
inline bool QXmlSimpleReaderPrivate::atEnd()
{
    return (c.unicode()|0x0001) == 0xffff;
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7604, as _ZN23QXmlSimpleReaderPrivate8initDataEv
inline void QXmlSimpleReaderPrivate::initData()
{
    c = QXmlInputSource::EndOfData;
    xmlRefStack.clear();
    next();
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 7615, as _ZNK23QXmlSimpleReaderPrivate11entityExistERK7QString
inline bool QXmlSimpleReaderPrivate::entityExist(const QString& e) const
{
    if ( parameterEntities.find(e) == parameterEntities.end() &&
          externParameterEntities.find(e) == externParameterEntities.end() &&
          externEntities.find(e) == externEntities.end() &&
          entities.find(e) == entities.end()) {
        return false;
    } else {
        return true;
    }
}

//  from ../qt5compat/src/core5/sax/qxml.cpp, line 6284, as _ZN23QXmlSimpleReaderPrivate29isExpandedEntityValueTooLargeEP7QString
inline bool QXmlSimpleReaderPrivate::isExpandedEntityValueTooLarge(QString *errorMessage)
{
    QString entityNameBuffer;

    // For every entity, check how many times all entity names were referenced in its value.
    for (QMap<QString,QString>::const_iterator toSearchIt = entities.constBegin();
         toSearchIt != entities.constEnd();
         ++toSearchIt) {
        const QString &toSearch = toSearchIt.key();

        // Don't check the same entities twice.
        if (!literalEntitySizes.contains(toSearch)) {
            // The amount of characters that weren't entity names, but literals, like 'X'.
            QString leftOvers = entities.value(toSearch);
            // How many times was entityName referenced by toSearch?
            for (QMap<QString,QString>::const_iterator referencedIt = entities.constBegin();
                 referencedIt != entities.constEnd();
                 ++referencedIt) {
                const QString &entityName = referencedIt.key();

                for (int i = 0; i < leftOvers.size() && i != -1; ) {
                    entityNameBuffer = QLatin1Char('&') + entityName + QLatin1Char(';');

                    i = leftOvers.indexOf(entityNameBuffer, i);
                    if (i != -1) {
                        leftOvers.remove(i, entityName.size() + 2);
                        // The entityName we're currently trying to find was matched in this string; increase our count.
                        ++referencesToOtherEntities[toSearch][entityName];
                    }
                }
            }
            literalEntitySizes[toSearch] = leftOvers.size();
        }
    }

    for (QHash<QString, QHash<QString, int> >::const_iterator entityIt = referencesToOtherEntities.constBegin();
         entityIt != referencesToOtherEntities.constEnd();
         ++entityIt) {
        const QString &entity = entityIt.key();

        QHash<QString, int>::iterator expandedIt = expandedSizes.find(entity);
        if (expandedIt == expandedSizes.end()) {
            expandedIt = expandedSizes.insert(entity, literalEntitySizes.value(entity));
            for (QHash<QString, int>::const_iterator referenceIt = entityIt->constBegin();
                 referenceIt != entityIt->constEnd();
                 ++referenceIt) {
                const QString &referenceTo = referenceIt.key();
                const int references = referencesToOtherEntities.value(entity).value(referenceTo);
                // The total size of an entity's value is the expanded size of all of its referenced entities, plus its literal size.
                *expandedIt += expandedSizes.value(referenceTo) * references + literalEntitySizes.value(referenceTo) * references;
            }

            if (*expandedIt > entityCharacterLimit) {
                if (errorMessage) {
                    *errorMessage = QString::fromLatin1("The XML entity \"%1\" expands to a string that is too large to process (%2 characters > %3).")
                        .arg(entity, QString::number(*expandedIt), QString::number(entityCharacterLimit));
                }
                return true;
            }
        }
    }
    return false;
}
//  -----------------------------------------------------------------------

//  QXmlSimpleReaderPrivate::~QXmlSimpleReaderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivateD1Ev(QXmlSimpleReaderPrivate *self) {
  delete self;
}

//  void QXmlSimpleReaderPrivate::initIncrementalParsing()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate22initIncrementalParsingEv(
    QXmlSimpleReaderPrivate *self) {
  self->initIncrementalParsing();
}

//  void QXmlSimpleReaderPrivate::stringClear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate11stringClearEv(
    QXmlSimpleReaderPrivate *self) {
  self->stringClear();
}

//  void QXmlSimpleReaderPrivate::nameClear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate9nameClearEv(
    QXmlSimpleReaderPrivate *self) {
  self->nameClear();
}

//  void QXmlSimpleReaderPrivate::refClear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate8refClearEv(
    QXmlSimpleReaderPrivate *self) {
  self->refClear();
}

//  void QXmlSimpleReaderPrivate::next()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate4nextEv(
    QXmlSimpleReaderPrivate *self) {
  self->next();
}

//  bool QXmlSimpleReaderPrivate::atEnd()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate5atEndEv(
    QXmlSimpleReaderPrivate *self) {
  return self->atEnd();
}

//  void QXmlSimpleReaderPrivate::initData()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QXmlSimpleReaderPrivate8initDataEv(
    QXmlSimpleReaderPrivate *self) {
  self->initData();
}

//  bool QXmlSimpleReaderPrivate::entityExist(const QString &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QXmlSimpleReaderPrivate11entityExistERK7QString(
    const QXmlSimpleReaderPrivate *self,
    const QString *a0) {
  return self->entityExist(*a0);
}

//  bool QXmlSimpleReaderPrivate::isExpandedEntityValueTooLarge(QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QXmlSimpleReaderPrivate29isExpandedEntityValueTooLargeEP7QString(
    QXmlSimpleReaderPrivate *self,
    QString *errorMessage) {
  return self->isExpandedEntityValueTooLarge(errorMessage);
}

//  QXmlSimpleReader *QXmlSimpleReaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QXmlSimpleReader *ritual_ZN23QXmlSimpleReaderPrivate6q_funcEv(
    QXmlSimpleReaderPrivate *self) {
  return self->q_func();
}

//  const QXmlSimpleReader *QXmlSimpleReaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QXmlSimpleReader *ritual_ZNK23QXmlSimpleReaderPrivate6q_funcEv(
    const QXmlSimpleReaderPrivate *self) {
  return self->q_func();
}
