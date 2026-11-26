//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qvalue3daxisformatter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qvalue3daxisformatter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QPainter>
#include <QtGui/QOpenGLContext>
#include <QtGui/QOffscreenSurface>
#include <QtGui/qquaternion.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QRegularExpression>
#include <QtCore/QLocale>
#include <QtDataVisualization/private/qvalue3daxisformatter_p.h>
#include <QtDataVisualization/private/qvalue3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 197, as _ZN5Utils14preParseFormatERK7QStringRS0_S3_RiRc
inline Utils::ParamType Utils::preParseFormat(const QString &format, QString &preStr, QString &postStr,
                                       int &precision, char &formatSpec)
{
    static QRegularExpression formatMatcher(QStringLiteral("^([^%]*)%([\\-\\+#\\s\\d\\.lhjztL]*)([dicuoxfegXFEG])(.*)$"));
    static QRegularExpression precisionMatcher(QStringLiteral("\\.(\\d+)"));

    Utils::ParamType retVal;

    QRegularExpressionMatch formatMatch = formatMatcher.match(format, 0);

    if (formatMatch.hasMatch()) {
        preStr = formatMatch.captured(1);
        // Six and 'g' are defaults in Qt API
        precision = 6;
        if (!formatMatch.captured(2).isEmpty()) {
            QRegularExpressionMatch precisionMatch = precisionMatcher.match(formatMatch.captured(2),
                                                                            0);
            if (precisionMatch.hasMatch())
                precision = precisionMatch.captured(1).toInt();
        }
        if (formatMatch.captured(3).isEmpty())
            formatSpec = 'g';
        else
            formatSpec = formatMatch.captured(3).at(0).toLatin1();
        postStr = formatMatch.captured(4);
        retVal = mapFormatCharToParamType(formatSpec);
    } else {
        retVal = ParamTypeUnknown;
        // The out parameters are irrelevant in unknown case
    }

    return retVal;
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 248, as _ZN5Utils18formatLabelSprintfERK10QByteArrayNS_9ParamTypeEd
inline QString Utils::formatLabelSprintf(const QByteArray &format, Utils::ParamType paramType, qreal value)
{
    switch (paramType) {
    case ParamTypeInt:
        return QString::asprintf(format.constData(), qint64(value));
    case ParamTypeUInt:
        return QString::asprintf(format.constData(), quint64(value));
    case ParamTypeReal:
        return QString::asprintf(format.constData(), value);
    default:
        // Return format string to detect errors. Bars selection label logic also depends on this.
        return QString::fromUtf8(format);
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 263, as _ZN5Utils20formatLabelLocalizedENS_9ParamTypeEdRK7QLocaleRK7QStringS6_icRK10QByteArray
inline QString Utils::formatLabelLocalized(Utils::ParamType paramType, qreal value,
                                    const QLocale &locale, const QString &preStr, const QString &postStr,
                                    int precision, char formatSpec, const QByteArray &format)
{
    switch (paramType) {
    case ParamTypeInt:
    case ParamTypeUInt:
        return preStr + locale.toString(qint64(value)) + postStr;
    case ParamTypeReal:
        return preStr + locale.toString(value, formatSpec, precision) + postStr;
    default:
        // Return format string to detect errors. Bars selection label logic also depends on this.
        return QString::fromUtf8(format);
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 231, as _ZN5Utils24mapFormatCharToParamTypeEc
inline Utils::ParamType Utils::mapFormatCharToParamType(char formatSpec)
{
    ParamType retVal = ParamTypeUnknown;
    if (formatSpec == 'd' || formatSpec == 'i' || formatSpec == 'c') {
        retVal = ParamTypeInt;
    } else if (formatSpec == 'u' || formatSpec == 'o'
               || formatSpec == 'x'|| formatSpec == 'X') {
        retVal = ParamTypeUInt;
    } else if (formatSpec == 'f' || formatSpec == 'F'
               || formatSpec == 'e' || formatSpec == 'E'
               || formatSpec == 'g' || formatSpec == 'G') {
        retVal = ParamTypeReal;
    }

    return retVal;
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 311, as _ZN28QValue3DAxisFormatterPrivate11recalculateEv
inline void QValue3DAxisFormatterPrivate::recalculate()
{
    // Only recalculate if we need to and have m_axis pointer. If we do not have
    // m_axis, either we are not attached to an axis or this is a renderer cache.
    if (m_axis && m_needsRecalculate) {
        m_min = m_axis->min();
        m_max = m_axis->max();
        m_rangeNormalizer = (m_max - m_min);

        q_ptr->recalculate();
        m_needsRecalculate = false;
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 325, as _ZN28QValue3DAxisFormatterPrivate13doRecalculateEv
inline void QValue3DAxisFormatterPrivate::doRecalculate()
{
    int segmentCount = m_axis->segmentCount();
    int subGridCount = m_axis->subSegmentCount() - 1;
    QString labelFormat =  m_axis->labelFormat();

    m_gridPositions.resize(segmentCount + 1);
    m_subGridPositions.resize(segmentCount * subGridCount);

    m_labelPositions.resize(segmentCount + 1);
    m_labelStrings.clear();
    m_labelStrings.reserve(segmentCount + 1);

    // Use qreals for intermediate calculations for better accuracy on label values
    qreal segmentStep = 1.0 / qreal(segmentCount);
    qreal subSegmentStep = 0;
    if (subGridCount > 0)
        subSegmentStep = segmentStep / qreal(subGridCount + 1);

    // Calculate positions
    qreal rangeNormalizer = qreal(m_max - m_min);
    for (int i = 0; i < segmentCount; i++) {
        qreal gridValue = segmentStep * qreal(i);
        m_gridPositions[i] = float(gridValue);
        m_labelPositions[i] = float(gridValue);
        m_labelStrings << q_ptr->stringForValue(gridValue * rangeNormalizer + qreal(m_min),
                                                labelFormat);
        if (m_subGridPositions.size()) {
            for (int j = 0; j < subGridCount; j++)
                m_subGridPositions[i * subGridCount + j] = gridValue + subSegmentStep * (j + 1);
        }
    }

    // Ensure max value doesn't suffer from any rounding errors
    m_gridPositions[segmentCount] = 1.0f;
    m_labelPositions[segmentCount] = 1.0f;
    m_labelStrings << q_ptr->stringForValue(qreal(m_max), labelFormat);
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 364, as _ZN28QValue3DAxisFormatterPrivate12populateCopyER21QValue3DAxisFormatter
inline void QValue3DAxisFormatterPrivate::populateCopy(QValue3DAxisFormatter &copy)
{
    recalculate();
    q_ptr->populateCopy(copy);
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 370, as _ZN28QValue3DAxisFormatterPrivate14doPopulateCopyERS_
inline void QValue3DAxisFormatterPrivate::doPopulateCopy(QValue3DAxisFormatterPrivate &copy)
{
    copy.m_min = m_min;
    copy.m_max = m_max;
    copy.m_rangeNormalizer = m_rangeNormalizer;

    copy.m_gridPositions = m_gridPositions;
    copy.m_labelPositions = m_labelPositions;
    copy.m_subGridPositions = m_subGridPositions;
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 381, as _ZN28QValue3DAxisFormatterPrivate14stringForValueEdRK7QString
inline QString QValue3DAxisFormatterPrivate::stringForValue(qreal value, const QString &format)
{
    if (m_previousLabelFormat.compare(format)) {
        // Format string different than the previous one used, reparse it
        m_labelFormatArray = format.toUtf8();
        m_previousLabelFormat = format;
        m_preparsedParamType = Utils::preParseFormat(format, m_formatPreStr, m_formatPostStr,
                                                     m_formatPrecision, m_formatSpec);
    }

    if (m_cLocaleInUse) {
        return Utils::formatLabelSprintf(m_labelFormatArray, m_preparsedParamType, value);
    } else {
        return Utils::formatLabelLocalized(m_preparsedParamType, value, m_locale, m_formatPreStr,
                                           m_formatPostStr, m_formatPrecision, m_formatSpec,
                                           m_labelFormatArray);
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 400, as _ZNK28QValue3DAxisFormatterPrivate10positionAtEf
inline float QValue3DAxisFormatterPrivate::positionAt(float value) const
{
    return ((value - m_min) / m_rangeNormalizer);
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 405, as _ZNK28QValue3DAxisFormatterPrivate7valueAtEf
inline float QValue3DAxisFormatterPrivate::valueAt(float position) const
{
    return ((position * m_rangeNormalizer) + m_min);
}
//  -----------------------------------------------------------------------

//  A QValue3DAxisFormatterPrivate that Python can take functions over in. Every QValue3DAxisFormatterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValue3DAxisFormatterPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValue3DAxisFormatterPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQValue3DAxisFormatterPrivate : public QValue3DAxisFormatterPrivate {
public:
  using QValue3DAxisFormatterPrivate::QValue3DAxisFormatterPrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQValue3DAxisFormatterPrivateCall0 call = reinterpret_cast<CuteQValue3DAxisFormatterPrivateCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQValue3DAxisFormatterPrivateCall1 call = reinterpret_cast<CuteQValue3DAxisFormatterPrivateCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQValue3DAxisFormatterPrivateCall2 call = reinterpret_cast<CuteQValue3DAxisFormatterPrivateCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQValue3DAxisFormatterPrivateCall3 call = reinterpret_cast<CuteQValue3DAxisFormatterPrivateCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQValue3DAxisFormatterPrivateCall4 call = reinterpret_cast<CuteQValue3DAxisFormatterPrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQValue3DAxisFormatterPrivateCall5 call = reinterpret_cast<CuteQValue3DAxisFormatterPrivateCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQValue3DAxisFormatterPrivateCall6 call = reinterpret_cast<CuteQValue3DAxisFormatterPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QValue3DAxisFormatterPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QValue3DAxisFormatterPrivate10metaObjectEv(
    const QValue3DAxisFormatterPrivate *self) {
  return self->metaObject();
}

//  void *QValue3DAxisFormatterPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QValue3DAxisFormatterPrivate11qt_metacastEPKc(
    QValue3DAxisFormatterPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QValue3DAxisFormatterPrivate::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QValue3DAxisFormatterPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QValue3DAxisFormatterPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QValue3DAxisFormatterPrivate::~QValue3DAxisFormatterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QValue3DAxisFormatterPrivateD1Ev(
    QValue3DAxisFormatterPrivate *self) {
  delete self;
}

//  void QValue3DAxisFormatterPrivate::recalculate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QValue3DAxisFormatterPrivate11recalculateEv(
    QValue3DAxisFormatterPrivate *self) {
  self->recalculate();
}

//  void QValue3DAxisFormatterPrivate::doRecalculate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QValue3DAxisFormatterPrivate13doRecalculateEv(
    QValue3DAxisFormatterPrivate *self) {
  self->doRecalculate();
}

//  void QValue3DAxisFormatterPrivate::populateCopy(QValue3DAxisFormatter
//      &copy)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QValue3DAxisFormatterPrivate12populateCopyER21QValue3DAxisFormatter(
    QValue3DAxisFormatterPrivate *self,
    QValue3DAxisFormatter *copy) {
  self->populateCopy(*copy);
}

//  void
//      QValue3DAxisFormatterPrivate::doPopulateCopy(QValue3DAxisFormatterPri
//      vate &copy)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QValue3DAxisFormatterPrivate14doPopulateCopyERS_(
    QValue3DAxisFormatterPrivate *self,
    QValue3DAxisFormatterPrivate *copy) {
  self->doPopulateCopy(*copy);
}

//  QString QValue3DAxisFormatterPrivate::stringForValue(qreal value, const
//      QString &format)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QValue3DAxisFormatterPrivate14stringForValueEdRK7QString(
    QValue3DAxisFormatterPrivate *self,
    qreal value,
    const QString *format) {
  return new QString(self->stringForValue(value, *format));
}

//  float QValue3DAxisFormatterPrivate::positionAt(float value) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QValue3DAxisFormatterPrivate10positionAtEf(
    const QValue3DAxisFormatterPrivate *self,
    float value) {
  return self->positionAt(value);
}

//  float QValue3DAxisFormatterPrivate::valueAt(float position) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QValue3DAxisFormatterPrivate7valueAtEf(
    const QValue3DAxisFormatterPrivate *self,
    float position) {
  return self->valueAt(position);
}

//  void QValue3DAxisFormatterPrivate::markDirtyNoLabelChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QValue3DAxisFormatterPrivate22markDirtyNoLabelChangeEv(
    QValue3DAxisFormatterPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QValue3DAxisFormatterPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "markDirtyNoLabelChange()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "markDirtyNoLabelChange()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQValue3DAxisFormatterPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValue3DAxisFormatterPrivate(
    QValue3DAxisFormatterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQValue3DAxisFormatterPrivate *>(self)->take(key, call);
}
