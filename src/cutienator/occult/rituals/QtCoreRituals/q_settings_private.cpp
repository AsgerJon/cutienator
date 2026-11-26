//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(settings)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qsettings.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstringview.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <optional>
#include <QtCore/QVariant>
#include <QtCore/QString>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsettings.h>
#include <QtCore/private/qsettings_p.h>
#include <QtCore/qcache.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdir.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlibraryinfo.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/private/qtools_p.h>
#ifndef QT_BOOTSTRAPPED
#include <QtCore/qsavefile.h>
#include <QtCore/qlockfile.h>
#endif
#ifdef Q_OS_VXWORKS
#  include <ioLib.h>
#endif
#include <algorithm>
#include <stdlib.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#  include <shlobj.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qsettings.cpp, line 299, as _ZN16QSettingsPrivate17beginGroupOrArrayERK14QSettingsGroup
inline void QSettingsPrivate::beginGroupOrArray(const QSettingsGroup &group)
{
    groupStack.push(group);
    const QString name = group.name();
    if (!name.isEmpty())
        groupPrefix += name + u'/';
}

//  from src/corelib/io/qsettings.cpp, line 312, as _ZNK16QSettingsPrivate9setStatusEN9QSettings6StatusE
inline void QSettingsPrivate::setStatus(QSettings::Status status) const
{
    if (status == QSettings::NoError || this->status == QSettings::NoError)
        this->status = status;
}

//  from src/corelib/io/qsettings.cpp, line 324, as _ZN16QSettingsPrivate13requestUpdateEv
inline void QSettingsPrivate::requestUpdate()
{
    if (!pendingChanges) {
        pendingChanges = true;
#ifndef QT_NO_QOBJECT
        Q_Q(QSettings);
        QCoreApplication::postEvent(q, new QEvent(QEvent::UpdateRequest));
#else
        update();
#endif
    }
}

//  from src/corelib/io/qsettings.cpp, line 318, as _ZN16QSettingsPrivate6updateEv
inline void QSettingsPrivate::update()
{
    flush();
    pendingChanges = false;
}

//  from src/corelib/io/qsettings.cpp, line 283, as _ZN16QSettingsPrivate12processChildE11QStringViewNS_9ChildSpecER5QListI7QStringE
inline void QSettingsPrivate::processChild(QStringView key, ChildSpec spec, QStringList &result)
{
    if (spec != AllKeys) {
        qsizetype slashPos = key.indexOf(u'/');
        if (slashPos == -1) {
            if (spec != ChildKeys)
                return;
        } else {
            if (spec != ChildGroups)
                return;
            key.truncate(slashPos);
        }
    }
    result.append(key.toString());
}

//  from src/corelib/io/qsettings.cpp, line 337, as _ZN16QSettingsPrivate23variantListToStringListERK5QListI8QVariantE
inline QStringList QSettingsPrivate::variantListToStringList(const QVariantList &l)
{
    QStringList result;
    result.reserve(l.size());
    for (const auto &v : l)
        result.append(variantToString(v));
    return result;
}

//  from src/corelib/io/qsettings.cpp, line 346, as _ZN16QSettingsPrivate23stringListToVariantListERK5QListI7QStringE
inline QVariant QSettingsPrivate::stringListToVariantList(const QStringList &l)
{
    QStringList outStringList = l;
    for (qsizetype i = 0; i < outStringList.size(); ++i) {
        const QString &str = outStringList.at(i);

        if (str.startsWith(u'@')) {
            if (str.size() < 2 || str.at(1) != u'@') {
                QVariantList variantList;
                variantList.reserve(l.size());
                for (const auto &s : l)
                    variantList.append(stringToVariant(s));
                return variantList;
            }
            outStringList[i].remove(0, 1);
        }
    }
    return outStringList;
}

//  from src/corelib/io/qsettings.cpp, line 366, as _ZN16QSettingsPrivate15variantToStringERK8QVariant
inline QString QSettingsPrivate::variantToString(const QVariant &v)
{
    QString result;

    switch (v.metaType().id()) {
        case QMetaType::UnknownType:
            result = "@Invalid()"_L1;
            break;

        case QMetaType::QByteArray: {
            QByteArray a = v.toByteArray();
            result = "@ByteArray("_L1 + QLatin1StringView(a) + u')';
            break;
        }

#if QT_CONFIG(shortcut)
        case QMetaType::QKeySequence:
#endif
        case QMetaType::QString:
        case QMetaType::LongLong:
        case QMetaType::ULongLong:
        case QMetaType::Int:
        case QMetaType::UInt:
        case QMetaType::Bool:
        case QMetaType::Float:
        case QMetaType::Double: {
            result = v.toString();
            if (result.contains(QChar::Null))
                result = "@String("_L1 + result + u')';
            else if (result.startsWith(u'@'))
                result.prepend(u'@');
            break;
        }
        case QMetaType::QRect: {
            QRect r = qvariant_cast<QRect>(v);
            result = QString::asprintf("@Rect(%d %d %d %d)", r.x(), r.y(), r.width(), r.height());
            break;
        }
        case QMetaType::QSize: {
            QSize s = qvariant_cast<QSize>(v);
            result = QString::asprintf("@Size(%d %d)", s.width(), s.height());
            break;
        }
        case QMetaType::QPoint: {
            QPoint p = qvariant_cast<QPoint>(v);
            result = QString::asprintf("@Point(%d %d)", p.x(), p.y());
            break;
        }

        default: {
#ifndef QT_NO_DATASTREAM
            QDataStream::Version version;
            const char *typeSpec;
            if (v.userType() == QMetaType::QDateTime) {
                version = QDataStream::Qt_5_6;
                typeSpec = "@DateTime(";
            } else {
                version = QDataStream::Qt_4_0;
                typeSpec = "@Variant(";
            }
            QByteArray a;
            {
                QDataStream s(&a, QIODevice::WriteOnly);
                s.setVersion(version);
                s << v;
            }

            result = QLatin1StringView(typeSpec)
                     + QLatin1StringView(a.constData(), a.size())
                     + u')';
#else
            Q_ASSERT(!"QSettings: Cannot save custom types without QDataStream support");
#endif
            break;
        }
    }

    return result;
}

//  from src/corelib/io/qsettings.cpp, line 447, as _ZN16QSettingsPrivate15stringToVariantERK7QString
inline QVariant QSettingsPrivate::stringToVariant(const QString &s)
{
    if (s.startsWith(u'@')) {
        if (s.endsWith(u')')) {
            if (s.startsWith("@ByteArray("_L1)) {
                return QVariant(QStringView{s}.sliced(11).chopped(1).toLatin1());
            } else if (s.startsWith("@String("_L1)) {
                return QVariant(QStringView{s}.sliced(8).chopped(1).toString());
            } else if (s.startsWith("@Variant("_L1)
                       || s.startsWith("@DateTime("_L1)) {
#ifndef QT_NO_DATASTREAM
                QDataStream::Version version;
                int offset;
                if (s.at(1) == u'D') {
                    version = QDataStream::Qt_5_6;
                    offset = 10;
                } else {
                    version = QDataStream::Qt_4_0;
                    offset = 9;
                }
                QByteArray a = QStringView{s}.sliced(offset).toLatin1();
                QDataStream stream(&a, QIODevice::ReadOnly);
                stream.setVersion(version);
                QVariant result;
                stream >> result;
                return result;
#else
                Q_ASSERT(!"QSettings: Cannot load custom types without QDataStream support");
#endif
            } else if (s.startsWith("@Rect("_L1)) {
                QStringList args = QSettingsPrivate::splitArgs(s, 5);
                if (args.size() == 4)
                    return QVariant(QRect(args[0].toInt(), args[1].toInt(), args[2].toInt(), args[3].toInt()));
            } else if (s.startsWith("@Size("_L1)) {
                QStringList args = QSettingsPrivate::splitArgs(s, 5);
                if (args.size() == 2)
                    return QVariant(QSize(args[0].toInt(), args[1].toInt()));
            } else if (s.startsWith("@Point("_L1)) {
                QStringList args = QSettingsPrivate::splitArgs(s, 6);
                if (args.size() == 2)
                    return QVariant(QPoint(args[0].toInt(), args[1].toInt()));
            } else if (s == "@Invalid()"_L1) {
                return QVariant();
            }

        }
        if (s.startsWith("@@"_L1))
            return QVariant(s.sliced(1));
    }

    return QVariant(s);
}

//  from src/corelib/io/qsettings.cpp, line 526, as _ZN16QSettingsPrivate15iniUnescapedKeyE14QByteArrayViewR7QString
inline bool QSettingsPrivate::iniUnescapedKey(QByteArrayView key, QString &result)
{
    const QString decoded = QString::fromUtf8(key);
    const qsizetype size = decoded.size();
    result.reserve(result.size() + size);
    qsizetype i = 0;
    bool lowercaseOnly = true;
    while (i < size) {
        char16_t ch = decoded.at(i).unicode();

        if (ch == '\\') {
            result += u'/';
            ++i;
            continue;
        }

        if (ch != '%' || i == size - 1) {
            QChar qch(ch);
            if (qch.isUpper())
                lowercaseOnly = false;
            result += qch;
            ++i;
            continue;
        }

        int numDigits = 2;
        qsizetype firstDigitPos = i + 1;

        ch = decoded.at(i + 1).unicode();
        if (ch == 'U') {
            ++firstDigitPos;
            numDigits = 4;
        }

        if (firstDigitPos + numDigits > size) {
            result += u'%';
            ++i;
            continue;
        }

        bool ok;
        ch = QStringView(decoded).sliced(firstDigitPos, numDigits).toUShort(&ok, 16);
        if (!ok) {
            result += u'%';
            ++i;
            continue;
        }

        QChar qch(ch);
        if (qch.isUpper())
            lowercaseOnly = false;
        result += qch;
        i = firstDigitPos + numDigits;
    }
    return lowercaseOnly;
}

//  from src/corelib/io/qsettings.cpp, line 841, as _ZN16QSettingsPrivate9splitArgsERK7QStringx
inline QStringList QSettingsPrivate::splitArgs(const QString &s, qsizetype idx)
{
    qsizetype l = s.size();
    Q_ASSERT(l > 0);
    Q_ASSERT(s.at(idx) == u'(');
    Q_ASSERT(s.at(l - 1) == u')');

    QStringList result;
    QString item;

    for (++idx; idx < l; ++idx) {
        QChar c = s.at(idx);
        if (c == u')') {
            Q_ASSERT(idx == l - 1);
            result.append(item);
        } else if (c == u' ') {
            result.append(item);
            item.clear();
        } else {
            item.append(c);
        }
    }

    return result;
}
//  -----------------------------------------------------------------------

//  A QSettingsPrivate that Python can take functions over in. Every QSettingsPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSettingsPrivateCall0)(const void *, const QString *, int *);
typedef void (*CuteQSettingsPrivateCall1)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQSettingsPrivateCall2)(const void *, int *);
typedef void (*CuteQSettingsPrivateCall3)(const void *, int *);
typedef void (*CuteQSettingsPrivateCall4)(const void *, int *);
typedef bool (*CuteQSettingsPrivateCall5)(const void *, int *);
typedef QString * (*CuteQSettingsPrivateCall6)(const void *, int *);
class CuteQSettingsPrivate : public QSettingsPrivate {
public:
  using QSettingsPrivate::QSettingsPrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSettingsPrivate6removeERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate3setERK7QStringRK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate5clearEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate4syncEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate5flushEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSettingsPrivate10isWritableEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSettingsPrivate8fileNameEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QSettingsPrivate::remove(const QString &key)
  void remove(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSettingsPrivateCall0 call = reinterpret_cast<CuteQSettingsPrivateCall0>(taken[0]);
      call(this, &key, &handled);
      if (handled) return;
    }
  }

  //  void QSettingsPrivate::set(const QString &key, const QVariant &value)
  void set(const QString &key, const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSettingsPrivateCall1 call = reinterpret_cast<CuteQSettingsPrivateCall1>(taken[1]);
      call(this, &key, &value, &handled);
      if (handled) return;
    }
  }

  //  void QSettingsPrivate::clear()
  void clear() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSettingsPrivateCall2 call = reinterpret_cast<CuteQSettingsPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSettingsPrivate::sync()
  void sync() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSettingsPrivateCall3 call = reinterpret_cast<CuteQSettingsPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSettingsPrivate::flush()
  void flush() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSettingsPrivateCall4 call = reinterpret_cast<CuteQSettingsPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QSettingsPrivate::isWritable() const
  bool isWritable() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSettingsPrivateCall5 call = reinterpret_cast<CuteQSettingsPrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QSettingsPrivate::fileName() const
  QString fileName() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSettingsPrivateCall6 call = reinterpret_cast<CuteQSettingsPrivateCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QSettings *QSettingsPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSettings *ritual_ZN16QSettingsPrivate6q_funcEv(QSettingsPrivate *self) {
  return self->q_func();
}

//  const QSettings *QSettingsPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSettings *ritual_ZNK16QSettingsPrivate6q_funcEv(
    const QSettingsPrivate *self) {
  return self->q_func();
}

//  QSettingsPrivate::~QSettingsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivateD1Ev(QSettingsPrivate *self) {
  delete self;
}

//  void QSettingsPrivate::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate6removeERK7QString(
    QSettingsPrivate *self,
    const QString *key) {
  self->remove(*key);
}

//  void QSettingsPrivate::set(const QString &key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate3setERK7QStringRK8QVariant(
    QSettingsPrivate *self,
    const QString *key,
    const QVariant *value) {
  self->set(*key, *value);
}

//  std::optional<QVariant> QSettingsPrivate::get(const QString &key) const
extern "C" Q_DECL_EXPORT
std::optional<QVariant> *ritual_ZNK16QSettingsPrivate3getERK7QString(
    const QSettingsPrivate *self,
    const QString *key) {
  return new std::optional<QVariant>(self->get(*key));
}

//  QStringList QSettingsPrivate::children(const QString &prefix, ChildSpec
//      spec) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QSettingsPrivate8childrenERK7QStringNS_9ChildSpecE(
    const QSettingsPrivate *self,
    const QString *prefix,
    QSettingsPrivate::ChildSpec spec) {
  return new QList<QString>(self->children(*prefix, spec));
}

//  void QSettingsPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate5clearEv(QSettingsPrivate *self) {
  self->clear();
}

//  void QSettingsPrivate::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate4syncEv(QSettingsPrivate *self) {
  self->sync();
}

//  void QSettingsPrivate::flush()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate5flushEv(QSettingsPrivate *self) {
  self->flush();
}

//  bool QSettingsPrivate::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSettingsPrivate10isWritableEv(
    const QSettingsPrivate *self) {
  return self->isWritable();
}

//  QString QSettingsPrivate::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QSettingsPrivate8fileNameEv(
    const QSettingsPrivate *self) {
  return new QString(self->fileName());
}

//  void QSettingsPrivate::beginGroupOrArray(const QSettingsGroup &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate17beginGroupOrArrayERK14QSettingsGroup(
    QSettingsPrivate *self,
    const QSettingsGroup *group) {
  self->beginGroupOrArray(*group);
}

//  void QSettingsPrivate::setStatus(QSettings::Status status) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QSettingsPrivate9setStatusEN9QSettings6StatusE(
    const QSettingsPrivate *self,
    QSettings::Status status) {
  self->setStatus(status);
}

//  void QSettingsPrivate::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate13requestUpdateEv(QSettingsPrivate *self) {
  self->requestUpdate();
}

//  void QSettingsPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate6updateEv(QSettingsPrivate *self) {
  self->update();
}

//  void QSettingsPrivate::processChild(QStringView key, ChildSpec spec,
//      QStringList &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSettingsPrivate12processChildE11QStringViewNS_9ChildSpecER5QListI7QStringE(
    const QString *key,
    QSettingsPrivate::ChildSpec spec,
    QStringList *result) {
  QSettingsPrivate::processChild(QStringView(*key), spec, *result);
}

//  QStringList QSettingsPrivate::variantListToStringList(const QVariantList
//      &l)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QSettingsPrivate23variantListToStringListERK5QListI8QVariantE(
    const QList<QVariant> *l) {
  return new QList<QString>(QSettingsPrivate::variantListToStringList(*l));
}

//  QVariant QSettingsPrivate::stringListToVariantList(const QStringList &l)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN16QSettingsPrivate23stringListToVariantListERK5QListI7QStringE(
    const QList<QString> *l) {
  return new QVariant(QSettingsPrivate::stringListToVariantList(*l));
}

//  QString QSettingsPrivate::variantToString(const QVariant &v)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QSettingsPrivate15variantToStringERK8QVariant(
    const QVariant *v) {
  return new QString(QSettingsPrivate::variantToString(*v));
}

//  QVariant QSettingsPrivate::stringToVariant(const QString &s)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN16QSettingsPrivate15stringToVariantERK7QString(
    const QString *s) {
  return new QVariant(QSettingsPrivate::stringToVariant(*s));
}

//  bool QSettingsPrivate::iniUnescapedKey(QByteArrayView key, QString
//      &result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSettingsPrivate15iniUnescapedKeyE14QByteArrayViewR7QString(
    const QByteArrayView *key,
    QString *result) {
  return QSettingsPrivate::iniUnescapedKey(*key, *result);
}

//  QStringList QSettingsPrivate::splitArgs(const QString &s, qsizetype idx)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QSettingsPrivate9splitArgsERK7QStringx(
    const QString *s,
    qsizetype idx) {
  return new QList<QString>(QSettingsPrivate::splitArgs(*s, idx));
}

//  a Python function taken by a CuteQSettingsPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSettingsPrivate(
    QSettingsPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSettingsPrivate *>(self)->take(key, call);
}

//  a std::optional<QVariant> a ritual of QSettingsPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSettingsPrivate__std_optional_QVariant(
    std::optional<QVariant> *self) {
  delete self;
}

#endif  // QT_CONFIG(settings)
