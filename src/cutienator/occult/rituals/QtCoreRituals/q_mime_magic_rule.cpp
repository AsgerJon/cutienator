//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimemagicrule_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  3. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimemagicrule_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmimemagicrule_p.h>
#include <QtCore/private/qmimetypeparser_p.h>
#include <QtCore/QList>
#include <QtCore/QDebug>
#include <QtCore/qendian.h>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <QtCore/private/qtools_p.h>
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

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 23, as local:qmimemagicrule.cpp:magicRuleTypes
static constexpr auto magicRuleTypes = qOffsetStringArray(
    "invalid",
    "string",
    "host16",
    "host32",
    "big16",
    "big32",
    "little16",
    "little32",
    "byte"
);

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 49, as _ZNK14QMimeMagicRuleeqERKS_
inline bool QMimeMagicRule::operator==(const QMimeMagicRule &other) const
{
    return m_type == other.m_type &&
           m_value == other.m_value &&
           m_startPos == other.m_startPos &&
           m_endPos == other.m_endPos &&
           m_mask == other.m_mask &&
           m_pattern == other.m_pattern &&
           m_number == other.m_number &&
           m_numberMask == other.m_numberMask &&
           m_matchFunction == other.m_matchFunction;
}

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 315, as _ZNK14QMimeMagicRule4maskEv
inline QByteArray QMimeMagicRule::mask() const
{
    QByteArray result = m_mask;
    if (m_type == String) {
        // restore '0x'
        result = "0x" + result.toHex();
    }
    return result;
}

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 325, as _ZNK14QMimeMagicRule7matchesERK10QByteArray
inline bool QMimeMagicRule::matches(const QByteArray &data) const
{
    const bool ok = m_matchFunction && (this->*m_matchFunction)(data);
    if (!ok)
        return false;

    // No submatch? Then we are done.
    if (m_subMatches.isEmpty())
        return true;

    //qDebug() << "Checking" << m_subMatches.count() << "sub-rules";
    // Check that one of the submatches matches too
    for ( QList<QMimeMagicRule>::const_iterator it = m_subMatches.begin(), end = m_subMatches.end() ;
          it != end ; ++it ) {
        if ((*it).matches(data)) {
            // One of the hierarchies matched -> mimetype recognized.
            return true;
        }
    }
    return false;


}

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 35, as _ZN14QMimeMagicRule4typeERK10QByteArray
inline QMimeMagicRule::Type QMimeMagicRule::type(const QByteArray &theTypeName)
{
    for (int i = String; i <= Byte; ++i) {
        if (theTypeName == magicRuleTypes.viewAt(i))
            return Type(i);
    }
    return Invalid;
}

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 63, as _ZN14QMimeMagicRule14matchSubstringEPKcxyyyS1_S1_
inline bool QMimeMagicRule::matchSubstring(const char *dataPtr, qsizetype dataSize, quint64 rangeStart,
                                    quint64 rangeLength, quint64 valueLength, const char *valueData,
                                    const char *mask)
{
    // The range and the value length can come straight out of the binary mime.cache, so
    // nothing can be assumed about them: rangeStart can point past the data, and the value
    // read at the last position of the range has to stay inside it, too.
    const quint64 size = quint64(dataSize);
    if (rangeStart >= size || valueLength == 0 || rangeLength == 0
        || valueLength > size - rangeStart)
        return false;
    // Clamp the range to the data that is actually there, so that rangeStart + rangeLength
    // neither overflows nor points past the end.
    rangeLength = qMin(rangeLength, size - rangeStart);

    // Size of searched data.
    // Example: value="ABC", rangeLength=3 -> we need 3+3-1=5 bytes (ABCxx,xABCx,xxABC would match)
    const quint64 dataNeeded = qMin(rangeLength + valueLength - 1, size - rangeStart);

    if (!mask) {
        // callgrind says QByteArray::indexOf is much slower, since our strings are typically too
        // short for be worth Boyer-Moore matching (1 to 71 bytes, 11 bytes on average).
        bool found = false;
        for (quint64 i = rangeStart; i < rangeStart + rangeLength; ++i) {
            if (i + valueLength > size)
                break;

            if (memcmp(valueData, dataPtr + i, size_t(valueLength)) == 0) {
                found = true;
                break;
            }
        }
        if (!found)
            return false;
    } else {
        bool found = false;
        const char *readDataBase = dataPtr + rangeStart;
        // Example (continued from above):
        // deviceSize is 4, so dataNeeded was max'ed to 4.
        // maxStartPos = 4 - 3 + 1 = 2, and indeed
        // we need to check for a match a positions 0 and 1 (ABCx and xABC).
        const quint64 maxStartPos = dataNeeded - valueLength + 1;
        for (quint64 i = 0; i < maxStartPos; ++i) {
            const char *d = readDataBase + i;
            bool valid = true;
            for (quint64 idx = 0; idx < valueLength; ++idx) {
                if (((*d++) & mask[idx]) != (valueData[idx] & mask[idx])) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                found = true;
                break;
            }
        }
        if (!found)
            return false;
    }
    //qDebug() << "Found" << value << "in" << searchedData;
    return true;
}

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 126, as _ZNK14QMimeMagicRule11matchStringERK10QByteArray
inline bool QMimeMagicRule::matchString(const QByteArray &data) const
{
    const int rangeLength = m_endPos - m_startPos + 1;
    return QMimeMagicRule::matchSubstring(data.constData(), data.size(), m_startPos, rangeLength, m_pattern.size(), m_pattern.constData(), m_mask.constData());
}
//  -----------------------------------------------------------------------

//  void QMimeMagicRule::swap(QMimeMagicRule &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMimeMagicRule4swapERS_(
    QMimeMagicRule *self,
    QMimeMagicRule *other) {
  self->swap(*other);
}

//  bool QMimeMagicRule::operator==(const QMimeMagicRule &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMimeMagicRuleeqERKS_(
    const QMimeMagicRule *self,
    const QMimeMagicRule *other) {
  return self->operator==(*other);
}

//  Type QMimeMagicRule::type() const
extern "C" Q_DECL_EXPORT
QMimeMagicRule::Type ritual_ZNK14QMimeMagicRule4typeEv(
    const QMimeMagicRule *self) {
  return self->type();
}

//  QByteArray QMimeMagicRule::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QMimeMagicRule5valueEv(const QMimeMagicRule *self) {
  return new QByteArray(self->value());
}

//  int QMimeMagicRule::startPos() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMimeMagicRule8startPosEv(const QMimeMagicRule *self) {
  return self->startPos();
}

//  int QMimeMagicRule::endPos() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMimeMagicRule6endPosEv(const QMimeMagicRule *self) {
  return self->endPos();
}

//  QByteArray QMimeMagicRule::mask() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QMimeMagicRule4maskEv(const QMimeMagicRule *self) {
  return new QByteArray(self->mask());
}

//  bool QMimeMagicRule::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMimeMagicRule7isValidEv(const QMimeMagicRule *self) {
  return self->isValid();
}

//  bool QMimeMagicRule::matches(const QByteArray &data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMimeMagicRule7matchesERK10QByteArray(
    const QMimeMagicRule *self,
    const QByteArray *data) {
  return self->matches(*data);
}

//  Type QMimeMagicRule::type(const QByteArray &type)
extern "C" Q_DECL_EXPORT
QMimeMagicRule::Type ritual_ZN14QMimeMagicRule4typeERK10QByteArray(
    const QByteArray *type) {
  return QMimeMagicRule::type(*type);
}

//  bool QMimeMagicRule::matchSubstring(const char *dataPtr, qsizetype
//      dataSize, quint64 rangeStart, quint64 rangeLength, quint64
//      valueLength, const char *valueData, const char *mask)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QMimeMagicRule14matchSubstringEPKcxyyyS1_S1_(
    const char *dataPtr,
    qsizetype dataSize,
    quint64 rangeStart,
    quint64 rangeLength,
    quint64 valueLength,
    const char *valueData,
    const char *mask) {
  return QMimeMagicRule::matchSubstring(
      dataPtr,
      dataSize,
      rangeStart,
      rangeLength,
      valueLength,
      valueData,
      mask);
}

//  bool QMimeMagicRule::matchString(const QByteArray &data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMimeMagicRule11matchStringERK10QByteArray(
    const QMimeMagicRule *self,
    const QByteArray *data) {
  return self->matchString(*data);
}

//  QMimeMagicRule::~QMimeMagicRule()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMimeMagicRuleD1Ev(QMimeMagicRule *self) {
  delete self;
}

//  QList<QMimeMagicRule>::QList()
extern "C" Q_DECL_EXPORT
QList<QMimeMagicRule> *ritual_list_make_QMimeMagicRule() {
  return new QList<QMimeMagicRule>();
}

//  void QList<QMimeMagicRule>::append(const QMimeMagicRule &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QMimeMagicRule(
    QList<QMimeMagicRule> *self,
    const QMimeMagicRule *element) {
  self->append(*element);
}

//  qsizetype QList<QMimeMagicRule>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QMimeMagicRule(
    const QList<QMimeMagicRule> *self) {
  return self->size();
}

//  const QMimeMagicRule &QList<QMimeMagicRule>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QMimeMagicRule *ritual_list_at_QMimeMagicRule(
    const QList<QMimeMagicRule> *self,
    long long index) {
  return new QMimeMagicRule(self->at(index));
}

//  QList<QMimeMagicRule>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QMimeMagicRule(QList<QMimeMagicRule> *self) {
  delete self;
}

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source (src/corelib/mimetypes/qmimemagicrule.cpp, line 132),
//  because Qt's library carries the template under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  It is as Qt wrote it, with the word 'inline' put before it.

template <typename T>
inline bool QMimeMagicRule::matchNumber(const QByteArray &data) const
{
    const T value(m_number);
    const T mask(m_numberMask);

    const char *p = data.constData() + m_startPos;
    const char *e = data.constData() + qMin(data.size() - int(sizeof(T)), m_endPos);
    for ( ; p <= e; ++p) {
        if ((qFromUnaligned<T>(p) & mask) == (value & mask))
            return true;
    }

    return false;
}

//  -----------------------------------------------------------------------

//  bool QMimeMagicRule::matchNumber<quint8>(const QByteArray &data)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMimeMagicRule11matchNumberIhEEbRK10QByteArray(
    const QMimeMagicRule *self,
    const QByteArray *data) {
  return self->matchNumber<quint8>(*data);
}

//  bool QMimeMagicRule::matchNumber<quint16>(const QByteArray &data)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMimeMagicRule11matchNumberItEEbRK10QByteArray(
    const QMimeMagicRule *self,
    const QByteArray *data) {
  return self->matchNumber<quint16>(*data);
}

//  bool QMimeMagicRule::matchNumber<quint32>(const QByteArray &data)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMimeMagicRule11matchNumberIjEEbRK10QByteArray(
    const QMimeMagicRule *self,
    const QByteArray *data) {
  return self->matchNumber<quint32>(*data);
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
